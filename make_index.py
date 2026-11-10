"""重新生成 index.json：扫描每个文件夹里的 PLUGIN.md，读出 id/name/version/description，算 SHA-256。
新增或修改插件后运行：python make_index.py"""
import hashlib, json, pathlib

root = pathlib.Path(__file__).resolve().parent
plugins = []
for f in sorted(root.glob("*/PLUGIN.md")):
    raw = f.read_bytes()
    text = raw.decode("utf-8").replace("\r\n", "\n")
    head = text.split("---\n", 2)[1]
    meta = {k.strip(): v.strip() for k, v in (l.split(":", 1) for l in head.splitlines() if ":" in l)}
    plugins.append({
        "id": meta["id"], "name": meta["name"], "version": meta["version"],
        "description": meta.get("description", ""), "author": meta.get("author", ""),
        "file": f"{f.parent.name}/PLUGIN.md", "sha256": hashlib.sha256(raw).hexdigest(),
    })
(root / "index.json").write_text(json.dumps({"plugins": plugins}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"{len(plugins)} 个插件")
