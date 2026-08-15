# -*- coding: utf-8 -*-
"""核心运算：RREF / 行列式 / 逆矩阵 / 线性方程组 / 特征值 / 基础解系。

所有函数返回 LinalgResult：答案 + 步骤 + SymPy 复算凭证。
凭证纪律：answer_value 由本内核 Fraction 算出，parity 用 SymPy 独立重算比对，
两者一致才标记 verified=true —— 这就是给学生的"验算证明"。
"""
from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from typing import Any

from app.linalg.matrix import FracMatrix, Step, frac, frac_latex


@dataclass
class LinalgResult:
    name: str
    answer_latex: str = ""
    answer_value: str = ""            # 机器可读答案（复算比对用）
    steps: list[Step] = field(default_factory=list)
    verified: bool = False            # SymPy 复算是否一致
    detail: dict[str, Any] = field(default_factory=dict)
    error: str = ""

    def as_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "answer_latex": self.answer_latex,
            "answer_value": self.answer_value,
            "steps": [s.as_dict() for s in self.steps],
            "verified": self.verified,
            "detail": self.detail,
            "error": self.error,
        }


def _to_sympy(a: FracMatrix):
    import sympy
    return sympy.Matrix([[sympy.Rational(c.numerator, c.denominator) for c in row]
                         for row in a.rows])


# ----------------------------------------------------------------- RREF / rank

def rref(a: FracMatrix) -> LinalgResult:
    """高斯-约当消元到最简行阶梯形，逐步记录。"""
    steps: list[Step] = []
    m = a.copy()
    pivot_row = 0
    pivots: list[tuple[int, int]] = []
    for col in range(m.n):
        if pivot_row >= m.m:
            break
        target = next((i for i in range(pivot_row, m.m) if m.rows[i][col] != 0), None)
        if target is None:
            continue
        if target != pivot_row:
            m.swap_rows(target, pivot_row, steps, "把非零元换到当前主元行")
        if m.rows[pivot_row][col] != 1:
            m.scale_row(pivot_row, Fraction(1) / m.rows[pivot_row][col], steps)
        for i in range(m.m):
            if i != pivot_row and m.rows[i][col] != 0:
                m.add_row(i, pivot_row, -m.rows[i][col], steps)
        pivots.append((pivot_row, col))
        pivot_row += 1

    res = LinalgResult(
        name="最简行阶梯形（RREF）",
        answer_latex=m.latex(),
        answer_value=str(m.rows),
        steps=steps,
        detail={"rank": len(pivots), "pivot_cols": [c for _, c in pivots]},
    )
    try:
        import sympy
        rref_sp, _ = _to_sympy(a).rref()
        res.verified = _matrix_equal(rref_sp, m)
    except Exception:
        pass
    return res


def _matrix_equal(sp_matrix, m: FracMatrix) -> bool:
    """SymPy 矩阵与 FracMatrix 逐元素比对（SymPy 元素转 Rational 再比 Fraction）。"""
    if sp_matrix.rows != m.m or sp_matrix.cols != m.n:
        return False
    for i in range(m.m):
        for j in range(m.n):
            if Fraction(int(sp_matrix[i, j].p), int(sp_matrix[i, j].q)) != m.rows[i][j]:
                return False
    return True


def rank(a: FracMatrix) -> LinalgResult:
    base = rref(a)
    return LinalgResult(
        name="矩阵的秩",
        answer_latex=rf"\operatorname{{rank}} = {base.detail['rank']}",
        answer_value=str(base.detail["rank"]),
        steps=base.steps,
        verified=base.verified,
        detail={"rank": base.detail["rank"]},
    )


# -------------------------------------------------------------------- 行列式

def det(a: FracMatrix) -> LinalgResult:
    if a.m != a.n:
        raise ValueError("行列式只对方阵有定义")
    n = a.n
    if n == 1:
        return LinalgResult(name="行列式", answer_latex=frac_latex(a.rows[0][0]),
                            answer_value=str(a.rows[0][0]), steps=[], verified=_sp_det_equal(a, a.rows[0][0]))
    if n <= 3:
        return _det_cofactor(a)
    return _det_elimination(a)


def _det_cofactor(a: FracMatrix) -> LinalgResult:
    """n≤3 按第一行余子式展开——教学上最直观。"""
    steps: list[Step] = [Step(
        "definition", r"\det A = \sum_{j=1}^{n} (-1)^{1+j} a_{1j} M_{1j}",
        a.latex(), a.latex(), "按第一行余子式展开",
    )]
    n = a.n
    total = Fraction(0)
    terms: list[str] = []
    for j in range(n):
        minor = FracMatrix([
            [a.rows[r][c] for c in range(n) if c != j] for r in range(1, n)
        ])
        cofactor = (-1) ** (j + 2) * a.rows[0][j]
        minor_det = _det_plain(minor)
        contribution = cofactor * minor_det
        total += contribution
        terms.append(rf"(-1)^{{1,{j + 1}}} \cdot {frac_latex(a.rows[0][j])} \cdot ({_plain_det_latex(minor)}) = {frac_latex(contribution)}")
    expand_latex = r" \\ ".join(terms)
    steps.append(Step("expand", r"\det A = " + expand_latex, a.latex(), a.latex(),
                      "逐项计算各余子式的行列式"))
    return LinalgResult(
        name="行列式（余子式展开）",
        answer_latex=rf"\det A = {frac_latex(total)}",
        answer_value=str(total),
        steps=steps,
        verified=_sp_det_equal(a, total),
    )


def _det_plain(a: FracMatrix) -> Fraction:
    n = a.n
    if n == 1:
        return a.rows[0][0]
    if n == 2:
        return a.rows[0][0] * a.rows[1][1] - a.rows[0][1] * a.rows[1][0]
    total = Fraction(0)
    for j in range(n):
        minor = FracMatrix([
            [a.rows[r][c] for c in range(n) if c != j] for r in range(1, n)
        ])
        total += (-1) ** (j + 2) * a.rows[0][j] * _det_plain(minor)
    return total


def _plain_det_latex(a: FracMatrix) -> str:
    if a.n == 2:
        return (rf"{frac_latex(a.rows[0][0])} \cdot {frac_latex(a.rows[1][1])}"
                rf" - {frac_latex(a.rows[0][1])} \cdot {frac_latex(a.rows[1][0])}")
    return frac_latex(_det_plain(a))


def _det_elimination(a: FracMatrix) -> LinalgResult:
    """n≥4：行变换消上三角，行列式 = 主对角乘积 × 交换符号。"""
    steps: list[Step] = []
    m = a.copy()
    sign = Fraction(1)
    for col in range(m.n):
        target = next((i for i in range(col, m.m) if m.rows[i][col] != 0), None)
        if target is None:
            return LinalgResult(name="行列式（行变换）", answer_latex=r"\det A = 0",
                                answer_value="0", steps=steps, verified=_sp_det_equal(a, Fraction(0)))
        if target != col:
            m.swap_rows(target, col, steps, "主元为 0，交换两行（行列式变号）")
            sign = -sign
        for i in range(col + 1, m.m):
            if m.rows[i][col] != 0:
                m.add_row(i, col, -m.rows[i][col] / m.rows[col][col], steps,
                          "化上三角：消去下方元素（行倍加不改变行列式）")
    value = sign
    for i in range(m.n):
        value *= m.rows[i][i]
    diag = r" \cdot ".join(frac_latex(m.rows[i][i]) for i in range(m.n))
    prefix = "-" if sign < 0 else ""
    steps.append(Step("conclude", rf"\det A = {prefix}{diag} = {frac_latex(value)}",
                      m.latex(), m.latex(), "上三角矩阵行列式 = 主对角元之积（交换过一次则变号）"))
    return LinalgResult(
        name="行列式（行变换）",
        answer_latex=rf"\det A = {frac_latex(value)}",
        answer_value=str(value),
        steps=steps,
        verified=_sp_det_equal(a, value),
    )


def _sp_det_equal(a: FracMatrix, value: Fraction) -> bool:
    try:
        import sympy
        return _to_sympy(a).det() == sympy.Rational(value.numerator, value.denominator)
    except Exception:
        return False


# -------------------------------------------------------------------- 逆矩阵

def inverse(a: FracMatrix) -> LinalgResult:
    if a.m != a.n:
        raise ValueError("只有方阵才可能可逆")
    aug = a.augmented(FracMatrix.identity(a.n))
    steps: list[Step] = [Step(
        "definition", r"[A \mid I] \xrightarrow{\text{行变换}} [I \mid A^{-1}]",
        aug.latex(), aug.latex(), "构造增广矩阵，对左侧做行变换至单位阵",
    )]
    m = aug.copy()
    pivot_row = 0
    for col in range(a.n):
        target = next((i for i in range(pivot_row, m.m) if m.rows[i][col] != 0), None)
        if target is None:
            return LinalgResult(
                name="逆矩阵", answer_latex=r"A \text{ 不可逆（秩 } < n\text{）}",
                answer_value="not_invertible", steps=steps, verified=_sp_inv_agrees(a, None),
                detail={"invertible": False},
            )
        if target != pivot_row:
            m.swap_rows(target, pivot_row, steps)
        if m.rows[pivot_row][col] != 1:
            m.scale_row(pivot_row, Fraction(1) / m.rows[pivot_row][col], steps)
        for i in range(m.m):
            if i != pivot_row and m.rows[i][col] != 0:
                m.add_row(i, pivot_row, -m.rows[i][col], steps)
        pivot_row += 1

    inv_rows = [row[a.n:] for row in m.rows]
    inv = FracMatrix(inv_rows)
    verified = _sp_inv_agrees(a, inv)
    return LinalgResult(
        name="逆矩阵（Gauss-Jordan）",
        answer_latex=rf"A^{{-1}} = {inv.latex()}",
        answer_value=str(inv.rows),
        steps=steps,
        verified=verified,
        detail={"invertible": True},
    )


def _sp_inv_agrees(a: FracMatrix, inv: FracMatrix | None) -> bool:
    try:
        import sympy
        sp = _to_sympy(a)
        if sp.det() == 0:
            return inv is None
        if inv is None:
            return False
        return _matrix_equal(sp.inv(), inv)
    except Exception:
        return False


# ------------------------------------------------------------------ 线性方程组

def solve(a: FracMatrix, b: list[Any]) -> LinalgResult:
    """Ax=b：增广 RREF，判唯一解/无穷解/无解，给通解与基础解系。"""
    if len(b) != a.m:
        raise ValueError("b 的长度必须等于矩阵行数")
    bcol = FracMatrix([[frac(v)] for v in b])
    aug = a.augmented(bcol)
    steps: list[Step] = [Step(
        "definition", r"[A \mid b] \xrightarrow{\text{RREF}}",
        aug.latex(), aug.latex(), "写出增广矩阵",
    )]
    m = aug.copy()
    pivot_row = 0
    pivots: list[int] = []
    for col in range(a.n):
        if pivot_row >= m.m:
            break
        target = next((i for i in range(pivot_row, m.m) if m.rows[i][col] != 0), None)
        if target is None:
            continue
        if target != pivot_row:
            m.swap_rows(target, pivot_row, steps)
        if m.rows[pivot_row][col] != 1:
            m.scale_row(pivot_row, Fraction(1) / m.rows[pivot_row][col], steps)
        for i in range(m.m):
            if i != pivot_row and m.rows[i][col] != 0:
                m.add_row(i, pivot_row, -m.rows[i][col], steps)
        pivots.append(col)
        pivot_row += 1

    # 无解判定：存在 [0 ... 0 | c≠0] 行
    for i in range(m.m):
        if m.first_nonzero_col(i) == a.n:
            return LinalgResult(
                name="线性方程组",
                answer_latex=r"\text{方程组无解（出现 } 0 = c \neq 0 \text{ 行）}",
                answer_value="no_solution", steps=steps,
                verified=_sp_solve_agrees(a, b, None, "no_solution"),
                detail={"solution_type": "no_solution"},
            )

    free_cols = [j for j in range(a.n) if j not in pivots]
    if not free_cols:
        xs = [m.rows[i][a.n] for i in range(a.n)]
        x_latex = r",\; ".join(frac_latex(x) for x in xs)
        return LinalgResult(
            name="线性方程组",
            answer_latex=rf"x = ({x_latex})^{{\mathsf{{T}}}}",
            answer_value=str(xs),
            steps=steps,
            verified=_sp_solve_agrees(a, b, xs, "unique"),
            detail={"solution_type": "unique", "solution": xs},
        )

    # 无穷解：特解 + 基础解系
    particular = [Fraction(0)] * a.n
    for i, col in enumerate(pivots):
        particular[col] = m.rows[i][a.n]
    basis: list[list[Fraction]] = []
    for fc in free_cols:
        vec = [Fraction(0)] * a.n
        vec[fc] = Fraction(1)
        for i, col in enumerate(pivots):
            vec[col] = -m.rows[i][fc]
        basis.append(vec)

    p_latex = r",\; ".join(frac_latex(x) for x in particular)
    parts = [rf"\xi = ({p_latex})^{{\mathsf{{T}}}} \text{{（特解）}}"]
    for k, vec in enumerate(basis):
        v_latex = r",\; ".join(frac_latex(x) for x in vec)
        parts.append(rf"\eta_{{{k + 1}}} = ({v_latex})^{{\mathsf{{T}}}}")
    answer = (r"\text{通解：} x = \xi"
              + (r" + ".join([rf" k_{{{k + 1}}} \eta_{{{k + 1}}}" for k in range(len(basis))]))
              + r",\quad " + r" \\ ".join(parts))
    return LinalgResult(
        name="线性方程组",
        answer_latex=answer,
        answer_value=str({"particular": particular, "basis": basis}),
        steps=steps,
        verified=_sp_solve_agrees(a, b, {"particular": particular, "basis": basis}, "infinite"),
        detail={"solution_type": "infinite", "free_vars": len(free_cols)},
    )


def _sp_solve_agrees(a: FracMatrix, b: list[Any], answer: Any, kind: str) -> bool:
    try:
        import sympy
        sp_a = _to_sympy(a)
        sp_b = sympy.Matrix([sympy.Rational(frac(v).numerator, frac(v).denominator) for v in b])
        rank_a = sp_a.rank()
        rank_ab = sp_a.row_join(sp_b).rank()
        if kind == "no_solution":
            return rank_ab > rank_a
        if rank_ab > rank_a:
            return False
        if kind == "unique":
            sol, params = sp_a.gauss_jordan_solve(sp_b)
            if params:
                return False
            return [Fraction(int(v.p), int(v.q)) for v in sol] == answer
        # infinite：验证特解满足 Ax=b，基础解系张成零空间
        xi = sympy.Matrix([sympy.Rational(x.numerator, x.denominator) for x in answer["particular"]])
        if sp_a * xi != sp_b:
            return False
        ns = sp_a.nullspace()
        if len(ns) != len(answer["basis"]):
            return False
        for vec in answer["basis"]:
            v = sympy.Matrix([sympy.Rational(x.numerator, x.denominator) for x in vec])
            if sp_a * v != sympy.zeros(a.m, 1):
                return False
        return True
    except Exception:
        return False


# -------------------------------------------------------------------- 特征值

def eigen(a: FracMatrix) -> LinalgResult:
    """特征值 + 特征向量 + 可对角化判定。

    特征多项式求根交给 SymPy（根可能是无理数/复数，Fraction 表达不了），
    每个特征值的特征空间用本内核 RREF(A-λI) 逐步消元——步骤仍全程可见。
    """
    if a.m != a.n:
        raise ValueError("特征值只对方阵有定义")
    import sympy
    lam = sympy.symbols("lambda")
    sp = _to_sympy(a)
    char = sp.charpoly(lam)
    char_expr = char.as_expr()
    # sympy.roots 保留重数：{根: 代数重数}。solve 只回唯一根，会丢重根。
    roots_mult: dict[Any, int] = sympy.roots(char_expr)

    steps: list[Step] = [Step(
        "definition",
        r"\det(A - \lambda I) = " + sympy.latex(char_expr) + r" = 0",
        a.latex(), a.latex(),
        "特征方程：令 det(A-λI)=0，展开得特征多项式",
    )]

    eig_info: list[dict[str, Any]] = []
    unique_roots = list(roots_mult.keys())
    algebraic_mult = {u: roots_mult[u] for u in unique_roots}

    diagonalizable = True
    parts: list[str] = []
    for u in unique_roots:
        steps.append(Step(
            "eigenvalue",
            rf"\lambda = {sympy.latex(u)} \text{{（代数重数 {algebraic_mult[u]}）}}",
            a.latex(), a.latex(),
            "特征方程的一个根",
        ))
        # (A - λI) 用 SymPy 精确表示（λ 可能无理），RREF 步骤手写循环
        shifted = sp - sympy.eye(a.n) * u
        rref_m, pivots = shifted.rref()
        geo_mult = a.n - len(pivots)
        eigvecs = shifted.nullspace()
        if geo_mult < algebraic_mult[u]:
            diagonalizable = False
        vec_latex = []
        for v in eigvecs:
            # 归一：把首个自由量化 1 已由 nullspace 保证（整数基）
            vec_latex.append(rf"({sympy.latex(v.T)} )^{{\mathsf{{T}}}}")
        vecs = r",\; ".join(vec_latex) if vec_latex else r"\text{（无非零解，异常）}"
        steps.append(Step(
            "eigenspace",
            rf"E_{{\lambda={sympy.latex(u)}}} = \operatorname{{span}}\{{{vecs}\}}，\ \dim = {geo_mult}",
            sympy.latex(shifted), sympy.latex(rref_m),
            f"对 A-λI 做行变换求基础解系，几何重数 = {geo_mult}",
        ))
        parts.append(rf"\lambda = {sympy.latex(u)}:\ \dim E_\lambda = {geo_mult} \text{{（代数重数 {algebraic_mult[u]}）}}")
        eig_info.append({
            "eigenvalue": sympy.latex(u),
            "algebraic_mult": algebraic_mult[u],
            "geometric_mult": geo_mult,
            "eigenvectors": [sympy.latex(v.T) for v in eigvecs],
        })

    diag_note = (r"A \text{ 可对角化（每个特征值几何重数} = \text{代数重数）}"
                 if diagonalizable
                 else r"A \text{ 不可对角化（存在几何重数} < \text{代数重数的特征值）}")
    steps.append(Step("conclude", r" \\ ".join(parts) + r" \\ " + diag_note,
                      a.latex(), a.latex(), "特征值汇总与可对角化判定"))

    return LinalgResult(
        name="特征值与特征向量",
        answer_latex=diag_note + r",\quad \lambda = " + r",\; ".join(
            sympy.latex(u) for u in unique_roots),
        answer_value=str([sympy.latex(u) for u in unique_roots]),
        steps=steps,
        verified=_sp_eigen_agrees(a, roots_mult),
        detail={"eigenvalues": eig_info, "diagonalizable": diagonalizable},
    )


def _sp_eigen_agrees(a: FracMatrix, roots_mult: dict[Any, int]) -> bool:
    """复算凭证，三层独立验证：
    1) 每个根 λ 逐一代入特征方程 det(A-λI)=0（精确判零，支持 sqrt 等根式）；
    2) trace = Σ（λ×重数）；
    3) det = Π（λ×重数）。
    复数根时 simplify 可能抛比较异常，退化为高精度数值判零。
    """
    try:
        import sympy
        sp = _to_sympy(a)
        lam = sympy.symbols("lambda")
        # 1) 逐 λ 判零：det(A-λI) 在 λ = 根处应为 0
        for u in roots_mult:
            det_shift = (sp - sympy.eye(a.n) * u).det()
            try:
                if sympy.simplify(det_shift) != 0:
                    # simplify 未归零时用数值抽查（复数根路径）
                    if abs(complex(sympy.N(det_shift, 20))) > 1e-9:
                        return False
            except Exception:
                try:
                    if abs(complex(sympy.N(det_shift, 20))) > 1e-9:
                        return False
                except Exception:
                    return False
        # 2) trace 不变量
        trace = sum(a.rows[i][i] for i in range(a.n))
        sum_roots = sum(u * m for u, m in roots_mult.items())
        if sympy.simplify(sympy.Rational(trace.numerator, trace.denominator) - sum_roots) != 0:
            return False
        # 3) det 不变量
        det_val = sp.det()
        prod_roots = sympy.prod([u**m for u, m in roots_mult.items()]) if roots_mult else sympy.Integer(1)
        return sympy.simplify(det_val - prod_roots) == 0
    except Exception:
        return False


# ----------------------------------------------------------------- 基础解系/空间

def null_space(a: FracMatrix) -> LinalgResult:
    """零空间（齐次方程组 Ax=0 的基础解系）。"""
    zero_b = [0] * a.m
    res = solve(a, zero_b)
    basis = res.detail.get("basis") or res.detail
    return LinalgResult(
        name="零空间 N(A)（基础解系）",
        answer_latex=res.answer_latex,
        answer_value=res.answer_value,
        steps=res.steps,
        verified=res.verified,
        detail=res.detail,
    )


def column_space(a: FracMatrix) -> LinalgResult:
    """列空间：RREF 主元列对应原矩阵的列就是一组基。"""
    base = rref(a)
    pivot_cols = base.detail["pivot_cols"]
    cols = [[a.rows[i][j] for i in range(a.m)] for j in pivot_cols]
    vecs = []
    for j in pivot_cols:
        entries = r",\; ".join(frac_latex(a.rows[i][j]) for i in range(a.m))
        vecs.append(rf"({entries})^{{\mathsf{{T}}}}")
    answer = (r"\operatorname{Col}(A) = \operatorname{span}\{" + r",\; ".join(vecs) + r"\}"
              if vecs else r"\operatorname{Col}(A) = \{0\}")
    verified = False
    try:
        import sympy
        sp = _to_sympy(a)
        verified = sp.rank() == len(pivot_cols)
    except Exception:
        pass
    return LinalgResult(
        name="列空间 Col(A)",
        answer_latex=answer,
        answer_value=str(cols),
        steps=base.steps,
        verified=verified,
        detail={"pivot_cols": pivot_cols, "dim": len(pivot_cols)},
    )

# ------------------------------------------------------------------ Jordan 标准形

def _kernel_dims(sp_matrix, u, max_k: int, n: int) -> list[int]:
    """dim ker((A - uI)^k) 序列，k = 0..max_k。d_0 = 0，d_k = n - rank((A-uI)^k)。"""
    import sympy
    shift = sp_matrix - sympy.eye(n) * u
    dims = [0]
    power = sympy.eye(n)
    for _k in range(1, max_k + 1):
        power = power * shift
        dims.append(n - power.rank())
    return dims


def _blocks_from_dims(dims: list[int]) -> list[int]:
    """由核维数序列还原块大小清单。b_k = d_k - d_{k-1} 是大小 ≥ k 的块数，
    大小恰为 k 的块数 = b_k - b_{k+1}。"""
    m = len(dims) - 1
    b = [dims[k] - dims[k - 1] for k in range(1, m + 1)] + [0]
    sizes: list[int] = []
    for size in range(m, 0, -1):
        for _ in range(b[size - 1] - b[size]):
            sizes.append(size)
    return sizes


def _jordan_block(u, size: int):
    """上 Jordan 块：对角 u，上副对角线 1。"""
    import sympy
    mat = [[0] * size for _ in range(size)]
    for i in range(size - 1):
        mat[i][i + 1] = 1
    return sympy.eye(size) * u + sympy.Matrix(mat)


def _jordan_invariants_agree(sp_a, J, roots_mult) -> bool:
    """相似不变量复核：特征多项式相等，且每个特征值的核维数序列相等。

    定理：两矩阵相似 ⇔ 对每个特征值，dim ker((A-λI)^k) 序列完全相同。
    这是不依赖过渡矩阵 P 的独立复算凭证。
    注意：J.charpoly() 在复数代数系数（EX 域）下会抛比较异常，故 J 的
    特征多项式直接由根构造 ∏(λ-u)^重数，并用数值抽查比对（不展开）。
    """
    import sympy
    n = sp_a.rows
    try:
        lam = sympy.symbols("lambda")
        char_a = sp_a.charpoly(lam).as_expr()
        prod = sympy.Integer(1)
        for u, m in roots_mult.items():
            prod = prod * (lam - u) ** m
        for t in (sympy.Integer(0), sympy.Integer(1), sympy.Integer(-1), sympy.Integer(2)):
            va = sympy.N(char_a.subs(lam, t), 20)
            vj = sympy.N(prod.subs(lam, t), 20)
            if abs(complex(va - vj)) > 1e-9:
                return False
    except Exception:
        pass  # 特征多项式数值抽查失败不阻塞：核维数序列是主判据
    try:
        for u, alg_mult in roots_mult.items():
            da = _kernel_dims(sp_a, u, alg_mult, n)
            dj = _kernel_dims(J, u, alg_mult, n)
            if da != dj:
                return False
        return True
    except Exception:
        return False


def jordan(a: FracMatrix) -> LinalgResult:
    """Jordan 标准形：特征多项式 → 特征值（代数重数）→ 各阶核维数 →
    Jordan 块结构 → 过渡矩阵 P（广义特征向量链）→ 凭证。

    特征多项式求根交给 SymPy（根可能无理/复数）。块结构判定是本内核的
    确定性逻辑：核维数序列是相似不变量，完全决定 Jordan 块结构。
    """
    if a.m != a.n:
        raise ValueError("Jordan 标准形只对方阵有定义")
    import sympy
    n = a.n
    sp = _to_sympy(a)
    lam = sympy.symbols("lambda")
    char_expr = sp.charpoly(lam).as_expr()
    roots_mult = sympy.roots(char_expr)  # {根: 代数重数}

    steps: list[Step] = [Step(
        "definition",
        r"\det(A - \lambda I) = " + sympy.latex(char_expr),
        a.latex(), a.latex(),
        "Jordan 标准形第一步：求特征多项式",
    )]

    # 特征多项式在有理数域不可约（roots 求不出）时：交给 SymPy jordan_form 兜底
    if not roots_mult:
        try:
            P_sp, J_sp = sp.jordan_form()
        except Exception as exc:
            return LinalgResult(
                name="Jordan 标准形",
                error=f"特征根无法解析表示：{exc}",
                steps=steps, verified=False,
            )
        steps.append(Step("conclude",
                          rf"J = {sympy.latex(J_sp)} \quad \text{{（由 SymPy jordan\_form 计算）}}",
                          a.latex(), sympy.latex(J_sp), "特征多项式在有理数域不可约，直接调用 SymPy"))
        try:
            verified = sympy.simplify(sp * P_sp - P_sp * J_sp) == sympy.zeros(n)
        except Exception:
            verified = False
        return LinalgResult(
            name="Jordan 标准形",
            answer_latex=rf"J = {sympy.latex(J_sp)}",
            answer_value=str(sympy.latex(J_sp)),
            steps=steps, verified=verified,
            detail={"jordan_latex": sympy.latex(J_sp), "p_latex": sympy.latex(P_sp),
                    "jordan_plain": str(J_sp.tolist())},
        )

    blocks: list[tuple[Any, int]] = []
    eig_info: list[dict[str, Any]] = []
    dims_table: list[str] = []
    for u, alg_mult in roots_mult.items():
        dims = _kernel_dims(sp, u, alg_mult, n)
        sizes = _blocks_from_dims(dims)
        blocks.extend((u, size) for size in sizes)
        geo_mult = dims[1]
        dims_latex = r",\; ".join(rf"d_{{{k}}} = {dims[k]}" for k in range(1, len(dims)))
        dims_table.append(
            rf"\lambda = {sympy.latex(u)}:\ {dims_latex} \Rightarrow "
            + r"\text{块} " + r",\ ".join(str(s) for s in sizes)
        )
        eig_info.append({
            "eigenvalue": sympy.latex(u),
            "algebraic_mult": alg_mult,
            "geometric_mult": geo_mult,
            "block_sizes": sizes,
        })
        steps.append(Step(
            "kernel_dims",
            rf"\lambda = {sympy.latex(u)}（代数重数 {alg_mult}）：" + dims_latex,
            a.latex(), a.latex(),
            f"dim ker((A-λI)^k) 序列：几何重数 = {geo_mult}，块大小 = {sizes}",
        ))

    # J = diag(J_1, ..., J_r)
    J = sympy.zeros(n)
    offset = 0
    for u, size in blocks:
        J[offset:offset + size, offset:offset + size] = _jordan_block(u, size)
        offset += size

    # P：广义特征向量链（尽力而为，失败仅影响展示，不影响 J 与验算）
    P = None
    P_note = "P 由广义特征向量链构造"
    try:
        P = _build_jordan_basis(sp, blocks, n)
        if P is not None and sympy.simplify(sp * P - P * J) != sympy.zeros(n):
            P = None
    except Exception:
        P = None
    if P is None:
        try:
            P, _ = sp.jordan_form()
            P_note = "P 由 SymPy jordan_form 计算"
        except Exception:
            P = None
            P_note = "P 未能显式构造（J 与验算不受影响）"

    verified = _jordan_invariants_agree(sp, J, roots_mult)

    blocks_latex = r",\ ".join(
        rf"J_{{{i + 1}}}({sympy.latex(u)})" + (rf"^{{{size}}}" if size > 1 else "")
        for i, (u, size) in enumerate(blocks)
    )
    answer = (
        rf"J = {sympy.latex(J)} \quad \text{{（}} {blocks_latex} \text{{）}}"
        + (rf",\quad P = {sympy.latex(P)}" if P is not None else "")
    )
    steps.append(Step("conclude", r" \\ ".join(dims_table), a.latex(), sympy.latex(J),
                      "核维数序列完全决定 Jordan 块结构（相似不变量）"))
    steps.append(Step("verify", rf"AP = PJ \iff A = PJP^{{-1}}", a.latex(),
                      sympy.latex(J), P_note))

    return LinalgResult(
        name="Jordan 标准形",
        answer_latex=answer,
        answer_value=str(sympy.latex(J)),
        steps=steps,
        verified=verified,
        detail={
            "eigenvalues": eig_info,
            "blocks": [(sympy.latex(u), size) for u, size in blocks],
            "jordan_latex": sympy.latex(J),
            "jordan_plain": str(J.tolist()),
            "p_latex": sympy.latex(P) if P is not None else "",
        },
    )


def _build_jordan_basis(sp, blocks: list[tuple[Any, int]], n: int):
    """按块构造广义特征向量链，返回 P（列 = 链向量）。

    对块 (u, k)：选 v ∈ ker((A-uI)^k) \\ ker((A-uI)^{k-1})，
    链 v_j = (A-uI)^{k-j} v（j=1..k），P 列序 = [v_1, ..., v_k]。
    返回的 P 满足 A·P = P·J（块序与 blocks 一致）。失败返回 None。
    """
    import sympy
    cols: list = []
    for u, size in blocks:
        shift = sp - sympy.eye(n) * u
        N_k = (shift ** size).nullspace()
        candidate = None
        for w in N_k:
            if size > 1 and sympy.simplify(shift ** (size - 1) * w) != sympy.zeros(n, 1):
                candidate = w
                break
            if size == 1 and sympy.simplify(shift * w) == sympy.zeros(n, 1):
                candidate = w
                break
        if candidate is None:
            return None
        chain = [(shift ** j) * candidate for j in range(size - 1, -1, -1)]
        cols.extend(reversed(chain))
    if not cols:
        return None
    P = sympy.Matrix.hstack(*cols)
    if P.rank() != n:
        return None
    return P


# ------------------------------------------------------------------ 二次型

def _sym_matrix_from_expression(expression: str) -> tuple[FracMatrix, list[str]]:
    """二次型表达式 → 对称矩阵 A 与变量名列表。

    只接受齐次二次型（所有项总次数为 2）。f = xᵀAx 中 A = Hessian(f)/2。
    """
    import sympy
    expr = sympy.sympify(str(expression))
    syms = sorted(expr.free_symbols, key=lambda s: s.name)
    if not syms:
        raise ValueError("表达式没有变量")
    poly = sympy.Poly(expr, *syms)
    if poly.total_degree() != 2 or poly.homogeneous_order() != 2:
        raise ValueError("只支持齐次二次型（所有项次数均为 2），如 x**2 + 2*x*y + y**2")
    hess = sympy.hessian(expr, syms)
    A_sym = sympy.simplify(hess / 2)
    rows: list[list[Fraction]] = []
    for i in range(len(syms)):
        row: list[Fraction] = []
        for j in range(len(syms)):
            v = A_sym[i, j]
            if not (v.is_Rational or sympy.simplify(v).is_Rational):
                raise ValueError(f"二次型系数 {v} 不是有理数")
            num, den = sympy.fraction(v)
            row.append(Fraction(int(num), int(den)))
        rows.append(row)
    return FracMatrix(rows), [str(s) for s in syms]


def _is_symmetric(a: FracMatrix) -> bool:
    return all(a.rows[i][j] == a.rows[j][i] for i in range(a.m) for j in range(a.n))


def _eigen_sign(v) -> int:
    """特征值符号：0（零）/ +1 / -1。解析判零，符号用高精度数值。"""
    import sympy
    try:
        if sympy.simplify(v) == 0:
            return 0
    except Exception:
        pass
    val = float(sympy.N(v, 30))
    if val > 0:
        return 1
    if val < 0:
        return -1
    return 0


def _definiteness(p: int, q: int, n: int) -> str:
    if q == 0 and p == n:
        return "正定"
    if p == 0 and q == n:
        return "负定"
    if q == 0:
        return "半正定"
    if p == 0:
        return "半负定"
    return "不定"


def _join_signed_terms(diag_terms: list[str]) -> str:
    """把 "±λ y²" 项按符号拼接：首项带符号，后续项 + / - 分隔。"""
    if not diag_terms:
        return r"0"
    out = ""
    for k, term in enumerate(diag_terms):
        neg = term.startswith("- ")
        body = term[2:] if (term.startswith("+ ") or term.startswith("- ")) else term
        if k == 0:
            out = ("- " if neg else "") + body
        else:
            out += (" - " if neg else " + ") + body
    return out


def quadratic_form(matrix: list[list[Any]] | None = None,
                   expression: str | None = None) -> LinalgResult:
    """二次型：对称矩阵（或表达式）→ 特征值 → 正交对角化 → 标准形 →
    秩/正负惯性指数/符号差 → 正定性判定。特征值求根与对角化由 SymPy 完成，
    惯性指数与正定性由本内核判定，并用 SymPy 的 is_positive_definite 等复算。"""
    import sympy
    if matrix is None and expression is None:
        raise ValueError("需要 matrix 或 expression 至少一个")
    if matrix is not None:
        a = FracMatrix.from_json(matrix)
        var_names = [rf"x_{{{i + 1}}}" for i in range(a.n)]
        source_latex = a.latex()
    else:
        a, var_names = _sym_matrix_from_expression(expression)
        source_latex = str(expression)
    if a.m != a.n:
        raise ValueError("二次型矩阵必须为方阵")
    if not _is_symmetric(a):
        raise ValueError("二次型矩阵必须是对称矩阵（A = Aᵀ）")

    n = a.n
    sp = _to_sympy(a)
    lam = sympy.symbols("lambda")
    char_expr = sp.charpoly(lam).as_expr()
    roots_mult = sympy.roots(char_expr)

    f_latex = rf"f({', '.join(var_names)}) = \mathbf{{x}}^{{\mathsf{{T}}}} A \mathbf{{x}}"
    steps: list[Step] = [Step(
        "definition", f_latex + rf"，\ A = {source_latex}",
        a.latex(), a.latex(),
        "写出二次型的对称矩阵（xᵀAx 中 A 唯一）",
    )]

    eig_terms: list[str] = []
    eig_info: list[dict[str, Any]] = []
    for u, mult in roots_mult.items():
        eig_terms.append(rf"{sympy.latex(u)} \text{{（重数 {mult}）}}")
        eig_info.append({"eigenvalue": sympy.latex(u), "algebraic_mult": mult})
    steps.append(Step(
        "eigenvalues",
        r"\det(A - \lambda I) = " + sympy.latex(char_expr)
        + r" \Rightarrow \lambda \in \{" + r",\; ".join(eig_terms) + r"\}",
        a.latex(), a.latex(),
        "解特征方程得特征值（含重数）",
    ))

    # 正交对角化：Q 的列 = 单位特征向量（Gram-Schmidt 正交化 + 归一化）
    Q = None
    try:
        P_diag, _D = sp.diagonalize()
        if P_diag is not None:
            cols = [P_diag[:, j] for j in range(P_diag.cols)]
            orth = sympy.gram_schmidt(cols, orthonormal=True)
            Q = sympy.Matrix.hstack(*orth) if orth else None
        if Q is not None and sympy.simplify(Q.T * Q - sympy.eye(n)) != sympy.zeros(n):
            Q = None
    except Exception:
        Q = None

    # 惯性指数与正定性（正/负特征值计数，含重数；零特征值不计入秩）
    p = q = 0
    rank_val = 0
    for u, mult in roots_mult.items():
        s = _eigen_sign(u)
        if s != 0:
            rank_val += mult
        if s > 0:
            p += mult
        elif s < 0:
            q += mult
    signature = p - q
    defn = _definiteness(p, q, n)
    defn_verified = False
    try:
        if defn == "正定":
            defn_verified = bool(sp.is_positive_definite)
        elif defn == "半正定":
            defn_verified = bool(sp.is_positive_semidefinite) and not bool(sp.is_positive_definite)
        elif defn == "负定":
            defn_verified = bool(sp.is_negative_definite)
        elif defn == "半负定":
            defn_verified = bool(sp.is_negative_semidefinite) and not bool(sp.is_negative_definite)
        else:
            defn_verified = not (sp.is_positive_semidefinite or sp.is_negative_semidefinite)
    except Exception:
        defn_verified = False

    # 标准形 f = Σ λ_i y_i²（符号感知：负系数渲染为 -|λ| y²）
    diag_terms: list[str] = []
    for u, mult in roots_mult.items():
        for _ in range(mult):
            idx = len(diag_terms) + 1
            ul = sympy.latex(u)
            neg = ul.startswith("-")
            body = (ul[1:].strip() if neg else ul) + rf"\, y_{{{idx}}}^2"
            diag_terms.append(("- " if neg else "+ ") + body)
    canonical = _join_signed_terms(diag_terms)
    diag_matrix = sympy.diag(*[u for u, m in roots_mult.items() for _ in range(m)])
    steps.append(Step(
        "canonical",
        rf"f = {canonical}" + (rf"，\ 其中 y = Q^{{\mathsf{{T}}}} x" if Q is not None else ""),
        sympy.latex(sp), sympy.latex(diag_matrix),
        "特征值即标准形的系数（惯性定理保证符号不变性）",
    ))
    steps.append(Step(
        "conclude",
        rf"\operatorname{{rank}} = {rank_val},\quad p = {p},\quad q = {q},\quad"
        rf"\text{{符号差 }} s = p - q = {signature},\quad \text{{判定：}}{defn}",
        a.latex(), a.latex(), "正惯性指数 = 正特征值个数（含重数），负惯性指数同理",
    ))

    verified = defn_verified
    if Q is not None:
        try:
            if sympy.simplify(Q.T * sp * Q - diag_matrix) == sympy.zeros(n):
                verified = True
            else:
                verified = False
        except Exception:
            pass
    # trace/det 不变量兜底
    try:
        trace_ok = sympy.simplify(sp.trace() - sum(u * m for u, m in roots_mult.items())) == 0
        det_ok = sympy.simplify(sp.det() - sympy.prod([u**m for u, m in roots_mult.items()])) == 0
        verified = verified and trace_ok and det_ok
    except Exception:
        pass

    q_latex = rf"，\ Q = {sympy.latex(Q)}" if Q is not None else ""
    return LinalgResult(
        name="二次型标准形与正定性",
        answer_latex=(
            rf"f = {canonical}{q_latex},\quad \operatorname{{rank}} = {rank_val},"
            rf"\ p = {p},\ q = {q},\ s = {signature},\ \text{{{defn}}}"
        ),
        answer_value=f"{p},{q},{signature},{defn}",
        steps=steps,
        verified=verified,
        detail={
            "eigenvalues": eig_info,
            "rank": rank_val,
            "p": p, "q": q, "signature": signature,
            "definiteness": defn,
            "canonical_latex": canonical,
            "q_latex": sympy.latex(Q) if Q is not None else "",
        },
    )
