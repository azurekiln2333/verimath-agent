"""可复现随机数：PCG32 + 常用采样器。

为什么不用 random 模块或 Math.random：教学场景要求"再来一次一模一样"和
"换个种子看是不是巧合"。Mersenne Twister 的 Python 实现和 JS 引擎的
Math.random 无法跨语言对齐，所以自己实现 PCG32 —— 算法短、状态小、
统计性质好，前后端同种子必出同序列。

seed 会写进 artifact spec 与 trace，任何一次模拟都能完整重放。
"""

from __future__ import annotations

from math import cos, log, pi, sin, sqrt

_MASK64 = (1 << 64) - 1
_MASK32 = (1 << 32) - 1
_MULT = 6364136223846793005
_INC = 1442695040888963407


class PCG32:
    """PCG-XSH-RR 32 位输出变体。O'Neill 2014。"""

    __slots__ = ("state", "inc", "_spare")

    def __init__(self, seed: int = 42, stream: int = 54) -> None:
        self.inc = ((stream << 1) | 1) & _MASK64
        self.state = 0
        self._next_uint32()
        self.state = (self.state + (seed & _MASK64)) & _MASK64
        self._next_uint32()
        self._spare: float | None = None   # Box-Muller 的备用值

    def _next_uint32(self) -> int:
        old = self.state
        self.state = (old * _MULT + self.inc) & _MASK64
        xorshifted = (((old >> 18) ^ old) >> 27) & _MASK32
        rot = (old >> 59) & 31
        return ((xorshifted >> rot) | (xorshifted << ((-rot) & 31))) & _MASK32

    def random(self) -> float:
        """[0, 1) 均匀。用 53 位有效位，与 IEEE754 双精度对齐。"""
        hi = self._next_uint32() >> 5      # 27 位
        lo = self._next_uint32() >> 6      # 26 位
        return (hi * 67108864.0 + lo) / 9007199254740992.0

    def uniform(self, low: float = 0.0, high: float = 1.0) -> float:
        return low + (high - low) * self.random()

    def randint(self, low: int, high: int) -> int:
        """[low, high] 闭区间整数。用取模去偏，保证均匀。"""
        span = high - low + 1
        if span <= 0:
            raise ValueError("high 必须 >= low")
        limit = _MASK32 - (_MASK32 % span)
        while True:
            v = self._next_uint32()
            if v <= limit:
                return low + v % span

    def normal(self, mu: float = 0.0, sigma: float = 1.0) -> float:
        """Box-Muller 极坐标形式。一次生成两个值，缓存一个下次用。"""
        if self._spare is not None:
            z = self._spare
            self._spare = None
            return mu + sigma * z
        while True:
            u1 = self.random()
            if u1 > 0.0:
                break
        u2 = self.random()
        r = sqrt(-2.0 * log(u1))
        self._spare = r * sin(2.0 * pi * u2)
        return mu + sigma * r * cos(2.0 * pi * u2)

    def exponential(self, scale: float = 1.0) -> float:
        """逆变换采样。排掉 u=0 防 log(0)。"""
        while True:
            u = self.random()
            if u > 0.0:
                return -scale * log(u)

    def bernoulli(self, p: float = 0.5) -> int:
        return 1 if self.random() < p else 0

    def binomial(self, n: int, p: float) -> int:
        """小 n 直接累加伯努利。教学场景 n 不大，不需要 BTPE。"""
        return sum(self.bernoulli(p) for _ in range(n))

    def poisson(self, lam: float) -> int:
        """Knuth 乘积法。lam 较小时够用；lam 大时改用正态近似。"""
        if lam <= 0.0:
            return 0
        if lam > 30.0:
            return max(0, round(self.normal(lam, sqrt(lam))))
        target = 2.718281828459045 ** (-lam)
        k, prod = 0, self.random()
        while prod > target:
            k += 1
            prod *= self.random()
        return k

    def choice(self, items: list) -> object:
        if not items:
            raise ValueError("items 不能为空")
        return items[self.randint(0, len(items) - 1)]

    def sample_from(self, population: list, size: int) -> list:
        """有放回抽样。Bootstrap 的基础操作。"""
        return [self.choice(population) for _ in range(size)]

    def shuffled(self, items: list) -> list:
        """Fisher-Yates。置换检验与 p-hacking 演示要用。"""
        out = list(items)
        for i in range(len(out) - 1, 0, -1):
            j = self.randint(0, i)
            out[i], out[j] = out[j], out[i]
        return out
