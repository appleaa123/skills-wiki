"""Skill: pixelle_video."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("pixelle-video")


_SKILLS: dict[str, dict] = {
    'web': {
        "description": '![Web UI界面](resources/webui.',
        "guidance": '![Web UI界面](resources/webui.png)',
    },
    '': {
        "description": '- ✅ **2026-01-26**: 新增「动作迁移」模块，上传参考视频和图片进行动作迁移\n- ✅ **2026-01-14**: 新增「数字人口播」和「图生视频」流水线，新增多语言 TTS 音色支持\n- ✅ **2026-01-06**: 新增 RunningHub 48G 显存机器调用支持\n- ✅ **2025-12-28**: 支持 RunningHub 并发限制可配置，优化 LLM 返回',
        "guidance": '- ✅ **2026-01-26**: 新增「动作迁移」模块，上传参考视频和图片进行动作迁移\n- ✅ **2026-01-14**: 新增「数字人口播」和「图生视频」流水线，新增多语言 TTS 音色支持\n- ✅ **2026-01-06**: 新增 RunningHub 48G 显存机器调用支持\n- ✅ **2025-12-28**: 支持 RunningHub 并发限制可配置，优化 LLM 返回结构化数据的逻辑\n- ✅ **2025-12-17**: 支持 ComfyUI API Key 配置，支持 Nano Banana 模型调用，API 接口支持模板自定义参数\n- ✅ **2025-12-10**: 侧边栏内置 FAQ，锁定 edge-tts 版本修复 TTS 服务不稳定问题\n- ✅ **2025-12-08**: 支持固定脚本多种分割方式(段落/行/句子)，优化模板选择交互逻辑支持直接预览选择\n- ✅ **2025-12-06**: 修复视频生成 API 返回 URL 路径处理，支持跨平台兼容\n- ✅ **2025-12-05**: 新增 Windows 整合包下载，优化图片与视频反推工作流\n- ✅ **2025-12-04**: 新增「自定义素材」功能，支持用户上传自己的照片和视频，AI 智能分析生成脚本\n- ✅ **2025-11-18**: 优化 RunningHub 服务调用支持并行处理，新增历史记录页面，支持批量创建视频任务',
    },
    '': {
        "description": '- ✅ **全自动生成** - 输入主题，自动生成完整视频\n- ✅ **AI 智能文案** - 根据主题智能创作解说词，无需自己写脚本\n- ✅ **AI 生成配图** - 每句话都配上精美的 AI 插图\n- ✅ **AI 生成视频** - 支持使用 AI 视频生成模型（如 WAN 2.',
        "guidance": '- ✅ **全自动生成** - 输入主题，自动生成完整视频\n- ✅ **AI 智能文案** - 根据主题智能创作解说词，无需自己写脚本\n- ✅ **AI 生成配图** - 每句话都配上精美的 AI 插图\n- ✅ **AI 生成视频** - 支持使用 AI 视频生成模型（如 WAN 2.1）创建动态视频内容\n- ✅ **AI 生成语音** - 支持 Edge-TTS、Index-TTS 等众多主流 TTS 方案\n- ✅ **背景音乐** - 支持添加 BGM，让视频更有氛围\n- ✅ **视觉风格** - 多种模板可选，打造独特视频风格\n- ✅ **灵活尺寸** - 支持竖屏、横屏等多种视频尺寸\n- ✅ **多种 AI 模型** - 支持 GPT、通义千问、DeepSeek、Ollama 等\n- ✅ **原子能力灵活组合** - 基于 ComfyUI 架构，可使用预置工作流，也可自定义任意能力（如替换生图模型为 FLUX、替换 TTS 为 ChatTTS 等）',
    },
    '': {
        "description": 'Pixelle-Video 采用模块化设计，整个视频生成流程清晰简洁：\n\n![视频生成流程图](resources/flow.',
        "guidance": 'Pixelle-Video 采用模块化设计，整个视频生成流程清晰简洁：\n\n![视频生成流程图](resources/flow.png)\n\n从输入文本到最终视频输出，整个流程简洁清晰：**文案生成 → 配图规划 → 逐帧处理 → 视频合成**\n\n每个环节都支持灵活定制，可选择不同的 AI 模型、音频引擎、视觉风格等，满足个性化创作需求。',
    },
    '': {
        "description": '以下是使用 Pixelle-Video 生成的实际案例，展示了不同主题和风格的视频效果：\n\n### 📱 扩展模块视频展示\n\n<table>\n<tr>\n<td width="33%">\n<h3>👤 数字人口播</h3>\n<video src="https://github.',
        "guidance": '以下是使用 Pixelle-Video 生成的实际案例，展示了不同主题和风格的视频效果：\n\n### 📱 扩展模块视频展示\n\n<table>\n<tr>\n<td width="33%">\n<h3>👤 数字人口播</h3>\n<video src="https://github.com/user-attachments/assets/7c122563-c2e0-4dcd-a73c-25ba1d4fa2dd" controls width="100%"></video>\n<p align="center"><b>韩语数字人口播</b></p>\n</td>\n<td width="33%">\n<h3>🖼️ 图生视频</h3>\n<video src="https://github.com/user-attachments/assets/5b4eef17-07d0-4bde-9748-2ed68cc9888e" controls width="100%"></video>\n<p align="center"><b>卡通视频</b></p>\n</td>\n<td width="33%">\n<h3>💃 动作迁移</h3>\n<video src="https://github.com/user-attachments/assets/7b1240bc-e965-434c-b343-118ec4793d4f" controls width="100%"></video>\n<p align="center"><b>跳舞小猫</b></p>\n</td>\n</tr>\n</table>\n\n\n### 📱 竖屏视频展示\n\n<table>\n<tr>\n<td width="33%">\n<h3>🌄 人文纪实类 - 视频默认模版</h3>\n<video src="https://github.com/user-attachments/assets/e6716c1d-78de-453d-84c2-10873c8c595f" controls width="100%"></video>\n<p align="center"><b>旅行路上的风景让人流连忘返</b></p>\n</td>\n<td width="33%">\n<h3>🔍 文化解构类 - 视频默认模版</h3>\n<video src="https://github.com/user-attachments/assets/f5de75f6-135a-4ab4-9f5f-079f649764d5" controls width="100%"></video>\n<p align="center"><b>Santa ID</b></p>\n</td>\n<td width="33%">\n<h3>🔭 科学思辨类 - 视频默认模版</h3>\n<video src="https://github.com/user-attachments/assets/ceb8b0df-8331-4e1f-88e7-db5b295a1c1d" controls width="100%"></video>\n<p align="center"><b>为什么我们还没有找到外星文明？</b></p>\n</td>\n</tr>\n<tr>\n<td width="33%">\n<h3>🌱 个人成长类 - 克隆音色</h3>\n<video src="https://github.com/user-attachments/assets/1bad9a49-df83-4905-9cc8-9a7640e9c7d8" controls width="100%"></video>\n<p align="center"><b>如何提升自己</b></p>\n</td>\n<td width="33%">\n<h3>🧠 深度思考类 - 默认模板</h3>\n<video src="https://github.com/user-attachments/assets/663b705a-2aea-44bc-b266-4bb27aa255a8" controls width="100%"></video>\n<p align="center"><b>如何理解反脆弱</b></p>\n</td>\n<td width="33%">\n<h3>🏯 历史文化类 - 固定画面</h3>\n<video src="https://github.com/user-attachments/assets/56e0a018-fa99-47eb-a97f-fc2fa8915724" controls width="100%"></video>\n<p align="center"><b>资治通鉴</b></p>\n</td>\n</tr>\n<tr>\n<td width="33%">\n<h3>☀️ 情感类 - 克隆音色</h3>\n<video src="https://github.com/user-attachments/assets/4687df95-dd21-4a7b-b01e-f33a7b646644" controls width="100%"></video>\n<p align="center"><b>冬日暖阳</b></p>\n</td>\n<td width="33%">\n<h3>📜 小说解说类 - 自创脚本</h3>\n<video src="https://github.com/user-attachments/assets/d354465e-3fa8-40b4-93e9-61ad75ef0697" controls width="100%"></video>\n<p align="center"><b>斗破苍穹</b></p>\n</td>\n<td width="33%">\n<h3>🧬 知识科普类 - Qwen生图</h3>\n<video src="https://github.com/user-attachments/assets/8ac21768-41ce-4d41-acdd-e3dd3eb9725a" controls width="100%"></video>\n<p align="center"><b>养生知识</b></p>\n</td>\n</tr>\n</table>\n\n### 🖥️ 横屏视频展示\n\n<table>\n<tr>\n<td width="50%">\n<h3>💰 副业赚钱 - 电影模板</h3>\n<video src="https://github.com/user-attachments/assets/c9209d4e-73a6-4b82-aaad-cf102248c9e2" controls width="100%"></video>\n<p align="center"><b>副业赚钱</b></p>\n</td>\n<td width="50%">\n<h3>🏛️ 历史解说 - 自定义模板</h3>\n<video src="https://github.com/user-attachments/assets/a767c452-d5f1-4cff-bb34-b80fff0d4c3e" controls width="100%"></video>\n<p align="center"><b>资治通鉴启示录</b></p>\n</td>\n</tr>\n</table>\n\n> 💡 **提示**: 这些视频都是通过输入一个主题关键词，由 AI 全自动生成的，无需任何视频剪辑经验！\n\n\n<div id="tutorial-start" />',
    },
    '': {
        "description": '### 🪟 Windows 一键整合包（推荐 Windows 用户使用）\n\n**无需安装 Python、uv 或 ffmpeg，一键开箱即用！**\n\n👉 **[下载 Windows 一键整合包](https://github.',
        "guidance": '### 🪟 Windows 一键整合包（推荐 Windows 用户使用）\n\n**无需安装 Python、uv 或 ffmpeg，一键开箱即用！**\n\n👉 **[下载 Windows 一键整合包](https://github.com/AIDC-AI/Pixelle-Video/releases/latest)**\n\n1. 下载最新的 Windows 一键整合包并解压\n2. 双击运行 `start.bat` 启动 Web 界面\n3. 浏览器会自动打开 http://localhost:8501\n4. 在「⚙️ 系统配置」中配置 LLM API 和图像生成服务\n5. 开始生成视频！\n\n> 💡 **提示**: 整合包已包含所有依赖，无需手动安装任何环境。首次使用只需配置 API 密钥即可。\n\n\n### 从源码安装（适合 macOS / Linux 用户或需要自定义的用户）\n\n#### 前置环境依赖\n\n在开始之前，需要先安装 Python 包管理器 `uv` 和视频处理工具 `ffmpeg`：\n\n##### 安装 uv\n\n请访问 uv 官方文档查看适合你系统的安装方法：  \n👉 **[uv 安装指南](https://docs.astral.sh/uv/getting-started/installation/)**\n\n安装完成后，在终端中运行 `uv --version` 验证安装成功。\n\n##### 安装 ffmpeg\n\n**macOS**\n```bash\nbrew install ffmpeg\n```\n\n**Ubuntu / Debian**\n```bash\nsudo apt update\nsudo apt install ffmpeg\n```\n\n**Windows**\n- 下载地址：https://ffmpeg.org/download.html\n- 下载后解压，将 `bin` 目录添加到系统环境变量 PATH 中\n\n安装完成后，在终端中运行 `ffmpeg -version` 验证安装成功。\n\n\n#### 第一步：下载项目\n\n```bash\ngit clone https://github.com/AIDC-AI/Pixelle-Video.git\ncd Pixelle-Video\n```\n\n#### 第二步：启动 Web 界面\n\n```bash\n# 使用 uv 运行（推荐，会自动安装依赖）\nuv run streamlit run web/app.py\n```\n\n浏览器会自动打开 http://localhost:8501\n\n#### 第三步：在 Web 界面配置\n\n首次使用时，展开「⚙️ 系统配置」面板，填写：\n- **LLM 配置**: 选择 AI 模型（如通义千问、GPT 等）并填入 API Key\n- **图像配置**: 如需生成图片，配置 ComfyUI 地址或 RunningHub API Key\n\n配置好后点击「保存配置」，就可以开始生成视频了！\n\n<div id="tutorial-end" />',
    },
    '': {
        "description": '打开 Web 界面后，你会看到三栏布局，下面详细讲解每个部分：\n\n\n### ⚙️ 系统配置（首次必填）\n\n首次使用时需要配置，点击展开「⚙️ 系统配置」面板：\n\n#### 1.',
        "guidance": '打开 Web 界面后，你会看到三栏布局，下面详细讲解每个部分：\n\n\n### ⚙️ 系统配置（首次必填）\n\n首次使用时需要配置，点击展开「⚙️ 系统配置」面板：\n\n#### 1. LLM 配置（大语言模型）\n用于生成视频文案的 AI。\n\n**快速选择预设**  \n- 通过下拉菜单选择预设模型（通义千问、GPT-4o、DeepSeek 等）\n- 选择后会自动填充 base_url 和 model\n- 点击「🔑 获取 API Key」链接去注册并获取密钥\n\n**手动配置**  \n- API Key: 填入你的密钥\n- Base URL: API 地址\n- Model: 模型名称\n\n#### 2. 图像配置\n用于生成视频配图的 AI。\n\n**本地部署（推荐）**  \n- ComfyUI URL: 本地 ComfyUI 服务地址（默认 http://127.0.0.1:8188）\n- 点击「测试连接」确认服务可用\n\n**云端部署**  \n- RunningHub API Key: 云端图像生成服务的密钥\n\n配置完成后点击「保存配置」。\n\n\n### 📝 内容输入（左侧栏）\n\n#### 生成模式\n- **AI 生成内容**: 输入主题，AI 自动创作文案\n  - 适合：想快速生成视频，让 AI 写稿\n  - 例如：「为什么要养成阅读习惯」\n- **固定文案内容**: 直接输入完整文案，跳过 AI 创作\n  - 适合：已有现成文案，直接生成视频\n\n#### 背景音乐（BGM）\n- **无 BGM**: 纯人声解说\n- **内置音乐**: 选择预置的背景音乐（如 default.mp3）\n- **自定义音乐**: 将你的音乐文件（MP3/WAV 等）放到 `bgm/` 文件夹\n- 点击「试听 BGM」可以预览音乐\n\n\n### 🎤 语音设置（中间栏）\n\n#### TTS 工作流\n- 从下拉菜单选择 TTS 工作流（支持 Edge-TTS、Index-TTS 等）\n- 系统会自动扫描 `workflows/` 文件夹中的 TTS 工作流\n- 如果懂 ComfyUI，可以自定义 TTS 工作流\n\n#### 参考音频（可选）\n- 上传参考音频文件用于声音克隆（支持 MP3/WAV/FLAC 等格式）\n- 适用于支持声音克隆的 TTS 工作流（如 Index-TTS）\n- 上传后可以直接试听\n\n#### 预览功能\n- 输入测试文本，点击「预览语音」即可试听效果\n- 支持使用参考音频进行预览\n\n\n### 🎨 视觉设置（中间栏）\n\n#### 图像生成\n决定 AI 生成什么风格的配图。\n\n**ComfyUI 工作流**  \n- 从下拉菜单选择图像生成工作流\n- 支持本地部署（selfhost）和云端（RunningHub）工作流\n- 默认使用 `image_flux.json`\n- 如果懂 ComfyUI，可以放自己的工作流到 `workflows/` 文件夹\n\n**图像尺寸**  \n- 设置生成图像的宽度和高度（单位：像素）\n- 默认 1024x1024，可根据需要调整\n- 注意：不同的模型对尺寸有不同的限制\n\n**提示词前缀（Prompt Prefix）**  \n- 控制图像的整体风格（语言需要是英文的）\n- 例如：Minimalist black-and-white matchstick figure style illustration, clean lines, simple sketch style\n- 点击「预览风格」可以测试效果\n\n#### 视频模板\n决定视频画面的布局和设计。\n\n**模板命名规范**  \n- `static_*.html`: 静态模板（无需AI生成媒体，纯文字样式）\n- `image_*.html`: 图片模板（使用AI生成的图片作为背景）\n- `video_*.html`: 视频模板（使用AI生成的视频作为背景）\n\n**使用方法**  \n- 从下拉菜单选择模板，按尺寸分组显示（竖屏/横屏/方形）\n- 点击「预览模板」可以自定义参数测试效果\n- 如果懂 HTML，可以在 `templates/` 文件夹创建自己的模板\n- 🔗 [查看所有模板效果图](https://aidc-ai.github.io/Pixelle-Video/zh/user-guide/templates/#_3)\n\n\n### 🎬 生成视频（右侧栏）\n\n#### 生成按钮\n- 配置好所有参数后，点击「🎬 生成视频」\n- 会显示实时进度（生成文案 → 生成配图 → 合成语音 → 合成视频）\n- 生成完成后自动显示视频预览\n\n#### 进度显示\n- 实时显示当前步骤\n- 例如：「分镜 3/5 - 生成插图」\n\n#### 视频预览\n- 生成完成后自动播放\n- 显示视频时长、文件大小、分镜数等信息\n- 视频文件保存在 `output/` 文件夹\n\n\n### ❓ 常见问题\n\n**Q: 第一次使用需要多久？**  \nA: 生成时长取决于视频分镜数量、网络状况和 AI 推理速度，通常几分钟内即可完成。\n\n**Q: 视频效果不满意怎么办？**  \nA: 可以尝试：\n1. 更换 LLM 模型（不同模型文案风格不同）\n2. 调整图像尺寸和提示词前缀（改变配图风格）\n3. 更换 TTS 工作流或上传参考音频（改变语音效果）\n4. 尝试不同的视频模板和尺寸\n\n**Q: 费用大概多少？**  \nA: **本项目完全支持免费运行！**\n\n- **完全免费方案**: LLM 使用 Ollama（本地运行）+ ComfyUI 本地部署 = 0 元\n- **推荐方案**: LLM 使用通义千问（成本极低，性价比高）+ ComfyUI 本地部署\n- **云端方案**: LLM 使用 OpenAI + 图像使用 RunningHub（费用较高但无需本地环境）\n\n**选择建议**：本地有显卡建议完全免费方案，否则推荐使用通义千问（性价比高）',
    },
    '': {
        "description": 'Pixelle-Video 的设计受到以下优秀开源项目的启发：\n\n- [Pixelle-MCP](https://github.',
        "guidance": 'Pixelle-Video 的设计受到以下优秀开源项目的启发：\n\n- [Pixelle-MCP](https://github.com/AIDC-AI/Pixelle-MCP) - ComfyUI MCP 服务器，让 AI 助手直接调用 ComfyUI\n- [MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) - 优秀的视频生成工具\n- [NarratoAI](https://github.com/linyqh/NarratoAI) - 影视解说自动化工具\n- [MoneyPrinterPlus](https://github.com/ddean2009/MoneyPrinterPlus) - 视频创作平台\n- [ComfyKit](https://github.com/puke3615/ComfyKit) - ComfyUI 工作流封装库\n\n感谢这些项目的开源精神！🙏',
    },
    '': {
        "description": '扫描下方二维码加入我们的社区，获取最新动态和技术支持：\n\n| 微信群 | Discord 社区 |\n| ---- | ---- |\n| <img src="resources/wechat.',
        "guidance": '扫描下方二维码加入我们的社区，获取最新动态和技术支持：\n\n| 微信群 | Discord 社区 |\n| ---- | ---- |\n| <img src="resources/wechat.png" alt="微信交流群" width="250" /> | <img src="resources/discord.png" alt="Discord 社区" width="250" /> |',
    },
    '': {
        "description": '- 🐛 **遇到问题**: 提交 [Issue](https://github.',
        "guidance": '- 🐛 **遇到问题**: 提交 [Issue](https://github.com/AIDC-AI/Pixelle-Video/issues)\n- 💡 **功能建议**: 提交 [Feature Request](https://github.com/AIDC-AI/Pixelle-Video/issues)\n- ⭐ **给个 Star**: 如果这个项目对你有帮助，欢迎给个 Star 支持一下！',
    },
    '': {
        "description": '本项目采用 Apache 2.',
        "guidance": '本项目采用 Apache 2.0 许可证，详情请查看 [LICENSE](LICENSE) 文件。',
    },
    'star-history': {
        "description": '[![Star History Chart](https://api.',
        "guidance": '[![Star History Chart](https://api.star-history.com/svg?repos=AIDC-AI/Pixelle-Video&type=Date)](https://star-history.com/#AIDC-AI/Pixelle-Video&Date)',
    },
}


@mcp.tool()
def list_pixelle_video_skills() -> dict:
    """List all available pixelle_video skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_pixelle_video_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific pixelle_video skill."""
    if not skill_name or str(skill_name).lower() in ["null", "none"]:
        skill_name = "start-here" if "start-here" in _SKILLS else next(iter(_SKILLS))
    skill_data = _SKILLS.get(skill_name, {"error": f"Unknown skill: {skill_name}"})
    try:
        from fastmcp.server.dependencies import get_http_request
        client_id = get_http_request().headers.get("x-client-id")
    except Exception:
        client_id = None
    if not client_id:
        from core.config import get_client_id
        client_id = get_client_id()
    hint = get_presentation_hint('pixelle_video', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@pixelle_video",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'pixelle_video',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
