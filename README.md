# Aeri 插件市场

插件是教 [Aeri](https://github.com/yuqtai/Aeri) 怎么用某个软件的**说明书**：一个 Markdown 文件，不是程序。Aeri 发现你要操作这个软件时，会把说明书交给大模型，照着用最快、最稳的办法去做。

在 Aeri 里：**设置 → 插件**，点“安装”即可；也可以直接说“装一下 Obsidian 插件”。

## 现有插件

| 插件 | 能做什么 |
|---|---|
| 思源笔记 | 记到今天的日记、新建文档、搜索笔记（走本机接口，不点界面） |
| 记事本 | 写入、读取、保存 |
| Obsidian | 新建笔记、追加到每日笔记、打开、搜索（走 obsidian:// 链接） |

## 写一个插件

1. 新建文件夹，放一个 `PLUGIN.md`：

   ```markdown
   ---
   id: my-app            # 英文、数字、- 和 _
   name: 我的软件
   version: 1.0.0
   description: 一句话说明能做什么
   match: MyApp.exe      # 前台是这个程序时自动启用，多个用逗号隔开
   keywords: 我的软件, myapp   # 用户的话里出现这些词时自动启用
   author: 你的名字
   ---
   正文：写给大模型看的操作说明。怎么做最快、哪里容易出错、做完怎么确认。
   ```

2. 正文里可以让 Aeri 用的工具：桌面控制（desktop_snapshot / desktop_set_value 等）、open_url（支持 `obsidian://` 这类软件链接）、`local_http`（只能访问本机接口）。
3. 需要软件的令牌时，写 `{{secret:文件#JSON指针}}`，Aeri 会在本机读取后填进请求，不会发给大模型。只能读用户目录下的文件；可以用 `|` 接着读，比如 `~/.config/siyuan/workspace.json#/0|/conf/conf.json#/api/token`。
4. 运行 `python make_index.py` 更新 `index.json`，提交 PR。

**审核标准**：说明书只能教 Aeri 完成用户要求的事；不能让它把内容发到外部、执行下载的程序，或者绕过确认。
