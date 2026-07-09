from app.protocol import extract_session_id, extract_user_text, sse_event


def test_extract_user_text_from_message_content():
    payload = {"message": {"role": "user", "content": "什么是中心极限定理？"}}
    assert extract_user_text(payload) == "什么是中心极限定理？"


def test_extract_session_id_prefers_header():
    assert extract_session_id({"sessionId": "body-session"}, "header-session") == "header-session"


def test_sse_event_contains_event_and_json_data():
    event = sse_event("status", {"ok": True})
    assert event.startswith("event: status\n")
    assert 'data: {"ok":true}' in event

