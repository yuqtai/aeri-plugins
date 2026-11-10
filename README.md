# Aeri plugin market

Plugins teach [Aeri](https://github.com/yuqtai/Aeri) how to use a specific app. Each plugin is a short **guide** written in Markdown, not a program: when you ask Aeri to do something in that app, it hands the guide to the language model, which follows the fastest reliable way it describes.

Install them in Aeri under **Settings → Plugins**, or just say "install the Spotify plugin".

## Plugins

| Plugin | What it does |
|---|---|
| Notepad | Write, read and save text (built into Aeri) |
| Obsidian | New notes, daily notes, open and search, via `obsidian://` links |
| SiYuan | Daily notes, new documents and search through SiYuan's local API |
| Spotify | Open searches and music via `spotify:` links; play, pause and skip |
| Outlook | Draft emails with `mailto:`; never sends without your confirmation |
| VS Code | Open files, folders and settings via `vscode://` links |
| Slack | Open workspaces, channels and DMs; drafts only, you send |
| Discord | Open channels and messages from copied links; drafts only |
| Telegram | Open chats via `tg://` and `t.me` links; drafts only |
| Zoom | Join meetings from your invitation links, after you confirm |
| Teams | Open chats with a drafted message, channels and meetings, after you confirm |
| Notion | Open pages and search your workspace |
| Microsoft To Do | Add and check tasks through the app |

## Write a plugin

1. Create a folder with a `PLUGIN.md`:

   ```markdown
   ---
   id: my-app            # letters, digits, - and _
   name: My App
   version: 1.0.0
   description: One line about what it can do
   match: MyApp.exe      # used automatically when this program is in front (comma-separated)
   keywords: my app, myapp   # used automatically when the user mentions these words
   author: Your name
   ---
   The guide: how to do things fastest, what tends to go wrong, how to confirm it worked.
   ```

2. Tools a guide can rely on: desktop control (`desktop_snapshot`, `desktop_set_value`, …), `open_url` (app links such as `obsidian://`, `spotify:`, `mailto:`), and `local_http` (only `127.0.0.1` / `localhost`).
3. If the app needs a local token, write `{{secret:FILE#JSON_POINTER}}`. Aeri reads it on the user's PC and puts it into the request; the model never sees it. Only files under the user's profile can be read, and `|` chains lookups, e.g. `~/.config/siyuan/workspace.json#/0|/conf/conf.json#/api/token`.
4. Run `python make_index.py` to update `index.json`, then open a pull request.

**Review rules:** a guide may only help Aeri do what the user asked. It must not send data elsewhere, run downloaded programs or skip confirmations; sending messages, emails, payments and joining calls always need the user's explicit OK. Cite the official documentation for every link format in your PR.
