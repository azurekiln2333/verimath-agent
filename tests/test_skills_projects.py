# -*- coding: utf-8 -*-
"""manifest 路由 + solution/courseware 骨架 + 状态机测试。"""
from pathlib import Path

from app.agents.router import TutorRouter
from app.projects import MAX_ATTEMPTS, ProjectStore
from app.skills.registry import route_for_query


class TestManifestRouting:
    def test_solution_route_by_matrix_keyword(self):
        assert route_for_query("求 [[2,1],[1,3]] 的逆矩阵") == "solution"
        assert TutorRouter().answer("求逆矩阵 [[2,1],[1,3]]").route == "solution"

    def test_courseware_route(self):
        assert route_for_query("帮我做一份特征值的课件") == "courseware"

    def test_exercise_route_preserved(self):
        assert route_for_query("出一道练习题") == "exercise"

    def test_method_selection_fallback_intact(self):
        assert TutorRouter().answer("两组成绩比较用什么检验？").route == "method_selection"

    def test_specific_beats_generic(self):
        # "求特征值" 是 solution，不能被 method_selection 的泛化词吃掉
        assert route_for_query("这道题求特征值") == "solution"


class TestSolutionSkeleton:
    def test_offline_kernel_direct_answer(self):
        text = TutorRouter().answer("求 [[2,1],[1,3]] 的行列式").text
        assert "5" in text
        assert "SymPy" in text or "复算" in text

    def test_offline_inverse_works(self):
        text = TutorRouter().answer("求 [[4,7],[2,6]] 的逆").text
        assert "\\frac" in text  # 分数逆矩阵有 frac

    def test_guide_without_matrix_literal(self):
        text = TutorRouter().answer("帮我求这道题的逆矩阵（矩阵在图片里）").text
        assert "逐步" in text
        assert "[[" in text  # 给出格式示例

    def test_bad_literal_falls_back_to_guide(self):
        text = TutorRouter().answer("求 [[1,2],[3]] 的行列式").text
        assert "SymPy" not in text or "逐步" in text


class TestCoursewareSkeleton:
    def test_offline_template_guide(self):
        response = TutorRouter().answer("做一份中心极限定理的讲义")
        assert response.route == "courseware"
        assert "七段式" in response.text or "骨架" in response.text


class TestProjectStore:
    def test_full_gate_flow(self, tmp_path: Path):
        store = ProjectStore(tmp_path / "projects.sqlite")
        pid = store.create("s1", "线代题")
        assert store.get(pid)["stage"] == "parse"
        assert store.advance(pid)["stage"] == "solve"
        # verify 门：未 verified 拒绝推进
        store.advance(pid)  # parse->solve 已过，这次 solve->verify
        gate = store.advance(pid)
        assert gate["ok"] is False
        assert "unverified" in gate["reason"]
        # verified 后放行
        store.set_verified(pid, True)
        assert store.advance(pid)["stage"] == "writeup"
        assert store.advance(pid)["ok"] is False  # 已是最终阶段

    def test_attempts_exhausted_blocks(self, tmp_path: Path):
        store = ProjectStore(tmp_path / "p.sqlite")
        pid = store.create("s2", "卡在 verify")
        store.advance(pid)  # -> solve
        store.advance(pid)  # -> verify
        results = [store.advance(pid) for _ in range(MAX_ATTEMPTS)]
        assert all(r["ok"] is False for r in results)
        assert store.get(pid)["status"] == "blocked"
        store.set_verified(pid, True)  # 即使后验通过，blocked 也拒绝
        assert store.advance(pid)["ok"] is False

    def test_attempts_reset_on_advance(self, tmp_path: Path):
        store = ProjectStore(tmp_path / "p.sqlite")
        pid = store.create("s3", "重试后通过")
        store.advance(pid)
        store.advance(pid)      # -> verify
        store.record_attempt(pid)
        store.set_verified(pid, True)
        assert store.advance(pid)["ok"] is True
        assert store.get(pid)["attempts"] == 0
