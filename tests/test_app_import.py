def test_fastapi_app_imports():
    import app.main

    assert app.main.app.title == "xiaoyi-a2a-stat-tutor"

