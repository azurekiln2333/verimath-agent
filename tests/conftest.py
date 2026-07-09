"""测试隔离：把 DATA_DIR 指向临时目录，避免测试污染真实 .data/ 库。

会话/学习记录持久化后，测试会真实写库；必须在导入 app（含 settings 单例）之前
设置 DATA_DIR。conftest 由 pytest 在收集测试模块前最先导入，故在模块顶层设置即可。
"""

from __future__ import annotations

import os
import tempfile
from pathlib import Path

# 必须在任何 `from app...` 之前执行：settings = Settings() 在导入期读取 DATA_DIR。
if not os.environ.get("KEEP_REAL_DATA_DIR"):
    _tmp = Path(tempfile.mkdtemp(prefix="xiaoyi-test-data-"))
    os.environ["DATA_DIR"] = str(_tmp)
