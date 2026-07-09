from app.main import _parse_numbered_cards


def test_parses_bare_number_with_dot():
    raw = "1. 讲了中心极限定理\n2. 说明了大数定律"
    assert _parse_numbered_cards(raw, 2) == {
        0: "讲了中心极限定理",
        1: "说明了大数定律",
    }


def test_parses_bracket_with_delimiter():
    raw = "[1]. 第一段摘要\n[2]： 第二段摘要"
    assert _parse_numbered_cards(raw, 2) == {
        0: "第一段摘要",
        1: "第二段摘要",
    }


def test_parses_bracket_space_without_delimiter():
    # 这是本轮修复的核心缺口：`[1] 摘要`（方括号+空格、无点）过去无法匹配。
    raw = "[1] 中心极限定理的适用条件\n[2] 方差估计为何除以 n-1"
    assert _parse_numbered_cards(raw, 2) == {
        0: "中心极限定理的适用条件",
        1: "方差估计为何除以 n-1",
    }


def test_parses_bracket_immediately_followed_by_text():
    raw = "[1]无空格紧跟正文"
    assert _parse_numbered_cards(raw, 1) == {0: "无空格紧跟正文"}


def test_ignores_out_of_range_and_prose_lines():
    # 越界编号丢弃；无编号的正文行不误吞；裸数字后必须有分隔符。
    raw = "这是一段说明文字\n3 个苹果和梨\n[5] 越界摘要\n1. 有效摘要"
    assert _parse_numbered_cards(raw, 2) == {0: "有效摘要"}
