"""Skill: tvc_director."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("tvc-director")


_SKILLS: dict[str, dict] = {
    '': {
        "description": '整个流程对应真实 TVC 广告制作的阶段：\n\n```\n"帮我做一条户外相机的30秒TVC"\n        ↓\n  Phase 1: 创意简报        ← 客户 Brief\n  Phase 2: 创意提案        ← 创意总监提案会\n  Phase 3: 视觉定调        ← 美术风格确认\n  Phase 4: 前期筹备        ← 选角试装 + 产品定妆 + 堪景\n  P',
        "guidance": '整个流程对应真实 TVC 广告制作的阶段：\n\n```\n"帮我做一条户外相机的30秒TVC"\n        ↓\n  Phase 1: 创意简报        ← 客户 Brief\n  Phase 2: 创意提案        ← 创意总监提案会\n  Phase 3: 视觉定调        ← 美术风格确认\n  Phase 4: 前期筹备        ← 选角试装 + 产品定妆 + 堪景\n  Phase 5: 分镜与拍摄      ← 分镜脚本 + 现场拍摄\n  Phase 6: 审片迭代        ← 导演审片 + 修改\n  Phase 7: 交付打包        ← 终版交付\n        ↓\n  可直接复制使用的多宫格分镜图片提示词、\n  视频提示词和创意方案文档\n```',
    },
    '': {
        "description": '- **类比真实 TVC 制片流程** — 选角试装、产品定妆照、场景堪景、分镜脚本、拍摄执行——每个环节都有对应的 AI 提示词产出物\n- **完整创意流水线** — 从一句话需求到可交付的分镜提示词和视频脚本，全程 AI 驱动\n- **8 种 TVC 叙事模型** — 痛点-解决、产品电影化拆解、品牌世界穿梭等，覆盖主流广告叙事\n- **电影级视觉系统** — 5 种画风预设（A-E）、12 ',
        "guidance": '- **类比真实 TVC 制片流程** — 选角试装、产品定妆照、场景堪景、分镜脚本、拍摄执行——每个环节都有对应的 AI 提示词产出物\n- **完整创意流水线** — 从一句话需求到可交付的分镜提示词和视频脚本，全程 AI 驱动\n- **8 种 TVC 叙事模型** — 痛点-解决、产品电影化拆解、品牌世界穿梭等，覆盖主流广告叙事\n- **电影级视觉系统** — 5 种画风预设（A-E）、12 种场景类型、精确到秒的运镜编排\n- **产品+品牌世界双线叙事** — 不只是产品特写，而是产品在真实场景中的交叉剪辑\n- **即拷即用** — 产出的提示词可直接粘贴到 Nano Banana Pro / Seedance，无需二次加工',
    },
    '': {
        "description": '### 汽车 TVC — 产品电影化拆解\n\nhttps://github.',
        "guidance": '### 汽车 TVC — 产品电影化拆解\n\nhttps://github.com/user-attachments/assets/541055ed-d716-4087-86e2-a27d375282ed\n\n### 香水 TVC — 品牌世界穿梭\n\nhttps://github.com/user-attachments/assets/df2d51af-acc2-4f34-a228-8b35ea754345',
    },
    'tvc': {
        "description": '以下是一个真实的端到端案例——从一张参考图到 15 秒成片。\n\n### Step 1 — 给一张参考图 + 一句话需求\n\n> "帮我做一条银色轿跑的 15 秒 TVC"\n\n<img src="https://github.',
        "guidance": '以下是一个真实的端到端案例——从一张参考图到 15 秒成片。\n\n### Step 1 — 给一张参考图 + 一句话需求\n\n> "帮我做一条银色轿跑的 15 秒 TVC"\n\n<img src="https://github.com/user-attachments/assets/0d774888-0dbb-4fb7-a861-ca3116b812b7" width="400" alt="参考图：银色轿跑" />\n\nAI 会自动进入完整创意流：需求拆解 → 创意构思 → 画风确认 → 资产生成 → 分镜 + 视频脚本。\n\n### Step 2 — AI 生成产品多视图提示词 → Nano Banana Pro 出图\n\nAI 输出产品多视图提示词，复制到 Nano Banana Pro（edit 模式，传入参考图），得到标准化的多角度产品图：\n\n<img src="https://github.com/user-attachments/assets/9d97df38-79f1-4a6a-a6bb-0fdbd731faca" width="600" alt="产品多视图" />\n\n### Step 3 — AI 生成 9 宫格分镜提示词 → Nano Banana Pro 出图\n\nAI 输出 3×3 多宫格分镜提示词（包含逐格构图、光影、运镜描述），复制到 Nano Banana Pro（edit 模式，传入多视图 + 环境图），得到完整分镜：\n\n<img src="https://github.com/user-attachments/assets/1ca54c8a-e1c2-4a13-8e67-461ea327f2ab" width="600" alt="9 宫格分镜" />\n\n### Step 4 — AI 生成视频提示词 → Seedance 生成视频\n\nAI 同步输出 Seedance Multi-Phase 视频提示词（5 Phase / 15s），配合多宫格作为首帧 + 产品多视图作为锚定，双图输入 Seedance 生成最终视频。\n\n### 产出物一览\n\n| 产出物 | 工具 | 用途 |\n|--------|------|------|\n| 产品多视图 | Nano Banana Pro (edit) | 产品锚定，供后续步骤引用 |\n| 9 宫格分镜图 | Nano Banana Pro (edit) | 视频首帧 + 视觉校对 |\n| Multi-Phase 视频脚本 | Seedance | 生成 15s 成片 |\n| 创意方案文档 | — | 完整创意 brief 存档 |',
    },
    '': {
        "description": '传统 AI 生成广告往往只是"产品 + 黑底 + 旋转"的无限循环。TVC Director 不同——它按真实 TVC 制片 SOP 组织提示词生成，让每条提示词都有明确的制作环节归属：\n\n- **叙事驱动** — 先确定叙事模型和创意方向，再生成视觉，不是无脑套模板\n- **双世界交叉剪辑** — 产品特写与品牌世界场景交织，像真正的 TVC 一样讲故事\n- **精确到秒的运镜设计** — 每一',
        "guidance": '传统 AI 生成广告往往只是"产品 + 黑底 + 旋转"的无限循环。TVC Director 不同——它按真实 TVC 制片 SOP 组织提示词生成，让每条提示词都有明确的制作环节归属：\n\n- **叙事驱动** — 先确定叙事模型和创意方向，再生成视觉，不是无脑套模板\n- **双世界交叉剪辑** — 产品特写与品牌世界场景交织，像真正的 TVC 一样讲故事\n- **精确到秒的运镜设计** — 每一格分镜都有明确的景别、角度、光影和转场逻辑\n- **渐进式人机协作** — 每个阶段都可以介入调整，不是一键出片的黑盒',
    },
    '': {
        "description": '### 1.',
        "guidance": '### 1. 产品电影化拆解（Cinematic Product Breakdown）\n\n产品是唯一主角，纯影棚，多 Phase 的产品微电影：\n\n- 零件悬浮拆解/精密组装动画\n- 材质微距：金属磨砂纹理、玻璃折射、碳纤维编织\n- 精确到秒的运镜编排：极慢拆解 → 爆发旋转 → 悬浮凝视 → 俯冲穿越\n- 光影叙事：低调影棚光、侧光勾勒轮廓、光随旋转流动\n\n### 2. 品牌世界穿梭（Brand World Crosscut）\n\n品牌世界和产品世界轮流出场，用 Match Cut 衔接：\n\n- 运动相机 → 跳伞、潜水、滑雪、攀岩\n- 越野车 → 盘山弯道、沙漠、雪地\n- 每个 Phase 完整待在一个世界里，通过匹配剪辑无缝切换\n\n### 3. 生活方式短片（Lifestyle Film）\n\n产品始终待在品牌世界中，不跳出去做影棚特写：\n\n- 跑鞋穿在脚上、手表戴在手腕、眼镜架在鼻梁\n- 通过运镜手法（低角度追拍、慢动作、景深变化）自然突出产品\n- 片尾集中做 Hero Shot 收束',
    },
    '': {
        "description": '### Cursor\n\n```bash\ngit clone https://github.',
        "guidance": '### Cursor\n\n```bash\ngit clone https://github.com/Ethanxwang/tvc-director.git ~/.cursor/skills/tvc-director\n```\n\n### Claude Code\n\n```bash\ngit clone https://github.com/Ethanxwang/tvc-director.git ~/.claude/skills/tvc-director\n```',
    },
    '': {
        "description": '| 模式 | 触发信号 | 说明 |\n|------|---------|------|\n| **A：完整 TVC 创意流** | "帮我做一条xx产品广告" | Brief → 创意 → 画风 → 资产 → 分镜 → 打包 |\n| **B：快速资产/提示词** | "帮我做一个产品 Hero Shot" | 跳过创意阶段，直接生成资产或关键帧提示词 |\n| **C：分镜转化** | 提供 TVC',
        "guidance": '| 模式 | 触发信号 | 说明 |\n|------|---------|------|\n| **A：完整 TVC 创意流** | "帮我做一条xx产品广告" | Brief → 创意 → 画风 → 资产 → 分镜 → 打包 |\n| **B：快速资产/提示词** | "帮我做一个产品 Hero Shot" | 跳过创意阶段，直接生成资产或关键帧提示词 |\n| **C：分镜转化** | 提供 TVC 分镜脚本 | 画风 → 资产 → 将分镜转化为关键帧提示词 |\n| **D：迭代修正** | "这张产品图xx不对" | 定位问题并提供修正版提示词 |',
    },
    'tvc': {
        "description": '| 模型 | 名称 | 核心逻辑 |\n|------|------|---------|\n| A | 痛点-解决 | 痛点场景 → 产品拯救 |\n| B | 产品电影化拆解 | 多 Phase 微电影逐步揭示卖点 |\n| C | 品牌世界穿梭 | 使用场景 ↔ 产品特写交叉剪辑 |\n| D | 生活方式短片 | 产品始终在场景中，运镜突出 |\n| E | 情感锚点 | 情感故事，产品为载体 |\n|',
        "guidance": '| 模型 | 名称 | 核心逻辑 |\n|------|------|---------|\n| A | 痛点-解决 | 痛点场景 → 产品拯救 |\n| B | 产品电影化拆解 | 多 Phase 微电影逐步揭示卖点 |\n| C | 品牌世界穿梭 | 使用场景 ↔ 产品特写交叉剪辑 |\n| D | 生活方式短片 | 产品始终在场景中，运镜突出 |\n| E | 情感锚点 | 情感故事，产品为载体 |\n| F | 蒙太奇揭示 | 视觉奇观 → 产品揭示 |\n| G | 前后对比 | 使用前后的强烈反差 |\n| H | 品牌宣言 | 价值观驱动，产品收束 |',
    },
    '': {
        "description": '```\nmy-tvc-project/\n├── concept.',
        "guidance": '```\nmy-tvc-project/\n├── concept.md                      # TVC 创意方案文档\n├── storyboard.md                   # 分镜脚本（如有）\n│\n├── assets/                         # 产品资产图提示词（Nano Banana Pro）\n│   └── prompts/\n│       ├── product-multiview.md\n│       ├── product-detail-01.md\n│       ├── env-01-extreme-sports.md\n│       └── ...\n│\n├── keyframes/                      # 分镜关键帧提示词（Nano Banana Pro）\n│   └── prompts/\n│       ├── grid-01-brand-world.md\n│       ├── grid-02-product-world.md\n│       ├── endframe.md\n│       └── ...\n│\n└── video-scripts/                  # Multi-Phase 视频提示词（Seedance）\n    ├── segment-01-brand-world.md\n    ├── segment-02-product-breakdown.md\n    └── ...\n```',
    },
    '': {
        "description": '1.',
        "guidance": '1. **产品多视图** — 将 `assets/prompts/product-multiview.md` 中的提示词复制到 Nano Banana Pro，选择 edit 模式，传入参考图\n2. **分镜关键帧** — 将 `keyframes/prompts/` 下的提示词复制到 Nano Banana Pro，edit 模式，传入多视图 + 环境图\n3. **视频脚本** — 将 `video-scripts/` 下的 Multi-Phase 脚本配合多宫格首帧 + 产品多视图，输入 Seedance 生成视频',
    },
    '': {
        "description": '知识库按真实广告制作的工种职责拆分，按需加载：\n\n| 工种 | 文件 | 对应真实制作环节 | 加载时机 |\n|------|------|---------------|---------|\n| 制片统筹 | `SKILL.',
        "guidance": '知识库按真实广告制作的工种职责拆分，按需加载：\n\n| 工种 | 文件 | 对应真实制作环节 | 加载时机 |\n|------|------|---------------|---------|\n| 制片统筹 | `SKILL.md` | 制片流程管控、阶段流转 | 始终加载 |\n| 创意总监 | `treatment.md` | 创意提案、叙事模型、品类策略、出镜决策 | 创意提案 |\n| 摄影指导 | `shot-language.md` | 镜头语言、画风体系、场景类型、构图范式 | 视觉定调 / 分镜 |\n| 制片组 | `pre-production.md` | 选角试装、产品定妆、堪景、资产一致性 | 前期筹备 |\n| 导演 | `storyboard.md` | 分镜脚本、视频脚本、产品拆解、品牌世界镜头 | 分镜与拍摄 |\n| 后期 | `delivery.md` | 输出格式、迭代调试（11 种常见失败模式） | 审片 / 交付 |',
    },
    'license': {
        "description": 'MIT.',
        "guidance": 'MIT',
    },
}


@mcp.tool()
def list_tvc_director_skills() -> dict:
    """List all available tvc_director skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_tvc_director_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific tvc_director skill."""
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
    hint = get_presentation_hint('tvc_director', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@tvc_director",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'tvc_director',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
