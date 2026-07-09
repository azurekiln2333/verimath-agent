# Vendored 前端资产清单

面板 `[app/panel_html.py](/E:/windows_ext/Desktop/华为智能体/xiaoyi-a2a-stat-tutor/app/panel_html.py:1)` 依赖以下本地静态资源，由 FastAPI `/static/vendor/` 提供。

约束：
- 只使用官方发布源
- 不依赖公网 CDN
- 不通过 npm 安装到项目
- 以固定版本产物直接入仓，并记录 SHA256

| 文件 | 组件 | 版本 | 官方来源 | SHA256 |
|---|---|---|---|---|
| `katex.min.js` | KaTeX | `0.17.0` | `https://github.com/KaTeX/KaTeX/releases/tag/v0.17.0` 的 `katex.zip` | `45FBE318FEA878FDC0A111913DC1F87894B2C439360D0228C086EF313F213EFC` |
| `katex.min.css` | KaTeX | `0.17.0` | 同上 | `A34AD8FC188E8F5A3AF7CEAA2A58D7210C6C9171335A15BFF2B48EBCD6A6F5B0` |
| `auto-render.min.js` | KaTeX contrib | `0.17.0` | `katex.zip` 内 `contrib/auto-render.min.js` | `E5372D199BCDAE8B4DE71D0F7CEBA72A4BA12774A27C60A6F1F77D03B3228EE4` |
| `markdown-it.min.js` | markdown-it | `14.3.0` | `https://registry.npmjs.org/markdown-it/-/markdown-it-14.3.0.tgz` 内 `package/dist/markdown-it.min.js` | `70FE17BD06C7FA819F03A1ED10957904318103624198845DC893B309BF495E28` |
| `purify.min.js` | DOMPurify | `3.4.11` | `https://registry.npmjs.org/dompurify/-/dompurify-3.4.11.tgz` 内 `package/dist/purify.min.js` | `DBABB5B205A333EC49C8C09E7FCA30EF66DF0523BB8BC0FA9EA843841F111DBD` |

## 放置结构

```text
app/static/vendor/
  katex.min.js
  katex.min.css
  auto-render.min.js
  markdown-it.min.js
  purify.min.js
  fonts/
  VENDOR.md
```

## 备注

- `fonts/` 来自 `KaTeX 0.17.0` 的预构建发布包，已完整拷入 `app/static/vendor/fonts/`。
- 当前字体目录共 `60` 个文件，`katex.min.css` 通过相对路径引用这些字体。
- 后续升级时必须同步更新版本号、来源链接和 SHA256。
