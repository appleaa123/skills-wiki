"""Skill: industry_master."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("industry-master")


_SKILLS: dict[str, dict] = {
    'industry-master': {
        "description": '|',
        "file": 'industry-master.md',
    },
    'output': {
        "description": '|',
        "file": 'output.md',
    },
    'luo-xiang-criminal-law': {
        "description": '罗翔 (中国政法大学刑事司法学院 / 刑法学研究所所长) 视角. 大众普法代表 + 法律哲学 + 法考刑法名师. 调用此 skill 时, 用罗翔框架做刑法基础理解 / 法律哲学 / 大众普法决策.',
        "file": 'luo-xiang-criminal-law.md',
    },
    'wang-liming-civil-code': {
        "description": '王利明 (中国人民大学法学院) 视角. 民法典核心起草 + 民事法权威 + 人格权独立成编立法贡献. 调用此 skill 时, 用王利明框架做民法典 / 民事法 / 人格权 / 侵权责任 / 民事解释论决策.',
        "file": 'wang-liming-civil-code.md',
    },
    'zhang-mingkai-criminal-law-academic': {
        "description": '张明楷 (清华大学法学院文科资深教授) 视角. 国内刑法学术代表 + 教材标准 (《刑法学》第七版) + 结果无价值论代表. 调用此 skill 时, 用张明楷框架做刑法学术解释 / 构成要件实质解释 / 罪名认定决策.',
        "file": 'zhang-mingkai-criminal-law-academic.md',
    },
    'luo-xiang-criminal-law-2': {
        "description": '罗翔 (中国政法大学刑事司法学院 / 刑法学研究所所长) 视角. 大众普法代表 + 法律哲学 + 法考刑法名师. 调用此 skill 时, 用罗翔框架做刑法基础理解 / 法律哲学 / 大众普法决策.',
        "file": 'luo-xiang-criminal-law-2.md',
    },
    'wang-liming-civil-code-2': {
        "description": '王利明 (中国人民大学法学院) 视角. 民法典核心起草 + 民事法权威 + 人格权独立成编立法贡献. 调用此 skill 时, 用王利明框架做民法典 / 民事法 / 人格权 / 侵权责任 / 民事解释论决策.',
        "file": 'wang-liming-civil-code-2.md',
    },
    'zhang-mingkai-criminal-law-academic-2': {
        "description": '张明楷 (清华大学法学院文科资深教授) 视角. 国内刑法学术代表 + 教材标准 (《刑法学》第七版) + 结果无价值论代表. 调用此 skill 时, 用张明楷框架做刑法学术解释 / 构成要件实质解释 / 罪名认定决策.',
        "file": 'zhang-mingkai-criminal-law-academic-2.md',
    },
    'output-2': {
        "description": '|',
        "file": 'output-2.md',
    },
    'bradley-sutton-helium10': {
        "description": 'Bradley Sutton (Helium 10 VP of Education) 视角. 数据驱动亚马逊运营方法论. 调用此 skill 时, 用 Bradley 的认知框架做 Amazon 运营 / 关键词 / PPC 决策.',
        "file": 'bradley-sutton-helium10.md',
    },
    'steve-chou-mwqhj': {
        "description": 'Steve Chou (My Wife Quit Her Job) 视角. 美国独立站 + 跨境老兵的长期主义方法论. 调用此 skill 时, 用 Steve 的认知框架做 DTC / 多平台决策.',
        "file": 'steve-chou-mwqhj.md',
    },
    'yang-meng-anker': {
        "description": '阳萌 (Anker 创始人 / CEO) 视角. 中国品牌出海方法论 — 长期主义 / 浅海战略 / 国际品牌三段论. 调用此 skill 时, 用阳萌的认知框架做品牌出海决策.',
        "file": 'yang-meng-anker.md',
    },
    'bradley-sutton-helium10-2': {
        "description": 'Bradley Sutton (Helium 10 VP of Education) 视角. 数据驱动亚马逊运营方法论. 调用此 skill 时, 用 Bradley 的认知框架做 Amazon 运营 / 关键词 / PPC 决策.',
        "file": 'bradley-sutton-helium10-2.md',
    },
    'steve-chou-mwqhj-2': {
        "description": 'Steve Chou (My Wife Quit Her Job) 视角. 美国独立站 + 跨境老兵的长期主义方法论. 调用此 skill 时, 用 Steve 的认知框架做 DTC / 多平台决策.',
        "file": 'steve-chou-mwqhj-2.md',
    },
    'yang-meng-anker-2': {
        "description": '阳萌 (Anker 创始人 / CEO) 视角. 中国品牌出海方法论 — 长期主义 / 浅海战略 / 国际品牌三段论. 调用此 skill 时, 用阳萌的认知框架做品牌出海决策.',
        "file": 'yang-meng-anker-2.md',
    },
    'output-3': {
        "description": '|',
        "file": 'output-3.md',
    },
    'beat-hintermann-taa': {
        "description": 'Beat Hintermann (Kantonsspital Baselland, Switzerland) 视角. 踝关节置换 (TAA) HINTEGRA 假体设计师 + 20 年长期 follow-up 数据 + Patient selection 派. 调用此 skill 时, 用 Hintermann 框架做终末期踝关节炎 / 置换 vs 融合 / 长期 follow-up 决策.',
        "file": 'beat-hintermann-taa.md',
    },
    'mark-glazebrook-achilles': {
        "description": 'Mark Glazebrook (Dalhousie University, Canada) 视角. 跟腱病 PhD + 关节镜专家 + COA 前主席. 调用此 skill 时, 用 Glazebrook 框架做跟腱病变 / 关节镜 / 循证治疗等级决策.',
        "file": 'mark-glazebrook-achilles.md',
    },
    'zhang-jianzhong-tongren': {
        "description": '张建中 (首都医科大学附属北京同仁医院足踝外科矫形中心) 视角. 国内足踝外科教父级代表. 拇外翻 + 平足 + 踝关节置换 + 中文圈本土化派. 调用此 skill 时, 用张建中框架做拇外翻 / 国内患者 / 中文圈实操决策.',
        "file": 'zhang-jianzhong-tongren.md',
    },
    'beat-hintermann-taa-2': {
        "description": 'Beat Hintermann (Kantonsspital Baselland, Switzerland) 视角. 踝关节置换 (TAA) HINTEGRA 假体设计师 + 20 年长期 follow-up 数据 + Patient selection 派. 调用此 skill 时, 用 Hintermann 框架做终末期踝关节炎 / 置换 vs 融合 / 长期 follow-up 决策.',
        "file": 'beat-hintermann-taa-2.md',
    },
    'mark-glazebrook-achilles-2': {
        "description": 'Mark Glazebrook (Dalhousie University, Canada) 视角. 跟腱病 PhD + 关节镜专家 + COA 前主席. 调用此 skill 时, 用 Glazebrook 框架做跟腱病变 / 关节镜 / 循证治疗等级决策.',
        "file": 'mark-glazebrook-achilles-2.md',
    },
    'zhang-jianzhong-tongren-2': {
        "description": '张建中 (首都医科大学附属北京同仁医院足踝外科矫形中心) 视角. 国内足踝外科教父级代表. 拇外翻 + 平足 + 踝关节置换 + 中文圈本土化派. 调用此 skill 时, 用张建中框架做拇外翻 / 国内患者 / 中文圈实操决策.',
        "file": 'zhang-jianzhong-tongren-2.md',
    },
    'output-4': {
        "description": '|',
        "file": 'output-4.md',
    },
    'guzhu-luzhiyuan': {
        "description": '|',
        "file": 'guzhu-luzhiyuan.md',
    },
    'jiang-lihui': {
        "description": '|',
        "file": 'jiang-lihui.md',
    },
    'ye-yunyan': {
        "description": '叶云燕视角. 平安寿险代理人体系销售方法论 living legend, 「事业宗教叙事 + 师徒制扩张」流派代表. 提供「主动筛客 + 极致服务 + 团队复制」式决策视角, 与独立经纪流派 (江立辉 / 明亚) 形成对位张力.',
        "file": 'ye-yunyan.md',
    },
    'output-5': {
        "description": '|',
        "file": 'output-5.md',
    },
    'output-6': {
        "description": '|',
        "file": 'output-6.md',
    },
    'esther-perel': {
        "description": 'Esther Perel 视角. 长期关系悖论派代表. Mating in Captivity + Eroticism + Modern Burden + 出轨现代解读. 调用此 skill 时, 用 Perel 框架做长期关系决策.',
        "file": 'esther-perel.md',
    },
    'john-gottman': {
        "description": 'John Gottman (Gottman Institute) 视角. 循证婚姻研究派代表. Four Horsemen + 5:1 Magic Ratio + Cascade Model. 调用此 skill 时, 用 Gottman 框架做关系健康度判断.',
        "file": 'john-gottman.md',
    },
    'sue-johnson-eft': {
        "description": 'Sue Johnson (EFT 创始人) 视角. 依恋驱动派代表. EFT 7 Conversations + Hold Me Tight + 依恋触发点. 调用此 skill 时, 用 EFT 框架做关系修复决策.',
        "file": 'sue-johnson-eft.md',
    },
    'esther-perel-2': {
        "description": 'Esther Perel 视角. 长期关系悖论派代表. Mating in Captivity + Eroticism + Modern Burden + 出轨现代解读. 调用此 skill 时, 用 Perel 框架做长期关系决策.',
        "file": 'esther-perel-2.md',
    },
    'john-gottman-2': {
        "description": 'John Gottman (Gottman Institute) 视角. 循证婚姻研究派代表. Four Horsemen + 5:1 Magic Ratio + Cascade Model. 调用此 skill 时, 用 Gottman 框架做关系健康度判断.',
        "file": 'john-gottman-2.md',
    },
    'sue-johnson-eft-2': {
        "description": 'Sue Johnson (EFT 创始人) 视角. 依恋驱动派代表. EFT 7 Conversations + Hold Me Tight + 依恋触发点. 调用此 skill 时, 用 EFT 框架做关系修复决策.',
        "file": 'sue-johnson-eft-2.md',
    },
    'output-7': {
        "description": '|',
        "file": 'output-7.md',
    },
    'aleyda-solis-orainti': {
        "description": 'Aleyda Solis (Orainti 创始人 + SEOFOMO + LearningSEO.io) 视角. Technical + 国际化 SEO 派代表. 调用此 skill 时, 用 Aleyda 框架做技术 + 跨语言 SEO 决策.',
        "file": 'aleyda-solis-orainti.md',
    },
    'brian-dean-backlinko': {
        "description": 'Brian Dean (Backlinko 创始人) 视角. Content-driven SEO 派代表. Skyscraper Technique + Pillar Cluster + 长内容 + 链接建设. 调用此 skill 时, 用 Brian Dean 框架做 SEO 决策.',
        "file": 'brian-dean-backlinko.md',
    },
    'rand-fishkin-moz': {
        "description": 'Rand Fishkin (Moz 创始人 + SparkToro) 视角. SEO 长期主义 + 跨平台视野 + 受众洞察派. 调用此 skill 时, 用 Rand 框架做战略级 SEO 决策.',
        "file": 'rand-fishkin-moz.md',
    },
    'aleyda-solis-orainti-2': {
        "description": 'Aleyda Solis (Orainti 创始人 + SEOFOMO + LearningSEO.io) 视角. Technical + 国际化 SEO 派代表. 调用此 skill 时, 用 Aleyda 框架做技术 + 跨语言 SEO 决策.',
        "file": 'aleyda-solis-orainti-2.md',
    },
    'brian-dean-backlinko-2': {
        "description": 'Brian Dean (Backlinko 创始人) 视角. Content-driven SEO 派代表. Skyscraper Technique + Pillar Cluster + 长内容 + 链接建设. 调用此 skill 时, 用 Brian Dean 框架做 SEO 决策.',
        "file": 'brian-dean-backlinko-2.md',
    },
    'rand-fishkin-moz-2': {
        "description": 'Rand Fishkin (Moz 创始人 + SparkToro) 视角. SEO 长期主义 + 跨平台视野 + 受众洞察派. 调用此 skill 时, 用 Rand 框架做战略级 SEO 决策.',
        "file": 'rand-fishkin-moz-2.md',
    },
    'output-8': {
        "description": '|',
        "file": 'output-8.md',
    },
    'dong-yuhui-dongfangzhenxuan': {
        "description": '董宇辉 / 东方甄选视角. 内容驱动直播代表. 调用此 skill 时, 用东方甄选「文化带货」框架做内容驱动直播决策.',
        "file": 'dong-yuhui-dongfangzhenxuan.md',
    },
    'juliang-qianchuan-official': {
        "description": '巨量千川官方方法论视角. 抖音电商核心广告平台官方思路 (并入抖音电商后, 重 ROI / GMV). 调用此 skill 时, 用千川官方框架做投流决策.',
        "file": 'juliang-qianchuan-official.md',
    },
    'luo-yonghao-jiaopengyou': {
        "description": '罗永浩 / 交个朋友视角. 店播头部 + 头部主播 IP 化方法论. 调用此 skill 时, 用交个朋友的认知框架做店播 / 主播 IP 决策.',
        "file": 'luo-yonghao-jiaopengyou.md',
    },
    'dong-yuhui-dongfangzhenxuan-2': {
        "description": '董宇辉 / 东方甄选视角. 内容驱动直播代表. 调用此 skill 时, 用东方甄选「文化带货」框架做内容驱动直播决策.',
        "file": 'dong-yuhui-dongfangzhenxuan-2.md',
    },
    'juliang-qianchuan-official-2': {
        "description": '巨量千川官方方法论视角. 抖音电商核心广告平台官方思路 (并入抖音电商后, 重 ROI / GMV). 调用此 skill 时, 用千川官方框架做投流决策.',
        "file": 'juliang-qianchuan-official-2.md',
    },
    'luo-yonghao-jiaopengyou-2': {
        "description": '罗永浩 / 交个朋友视角. 店播头部 + 头部主播 IP 化方法论. 调用此 skill 时, 用交个朋友的认知框架做店播 / 主播 IP 决策.',
        "file": 'luo-yonghao-jiaopengyou-2.md',
    },
    'output-9': {
        "description": '|',
        "file": 'output-9.md',
    },
    'gumai-jiahe-content': {
        "description": '古麦嘉禾创始团队视角. 内容驱动派代表方法论, 强调内容 IP 化 + 真实分享. 调用此 skill 时, 用古麦嘉禾的认知框架做小红书内容运营决策.',
        "file": 'gumai-jiahe-content.md',
    },
    'liu-siyi-qunxiang': {
        "description": '群响刘思毅视角. 操盘手社群头部 + 私域 + 矩阵派代表. 调用此 skill 时, 用刘思毅的认知框架做小红书操盘手 + 私域 + 矩阵决策.',
        "file": 'liu-siyi-qunxiang.md',
    },
    'qiangua-data-driven': {
        "description": '千瓜数据创始团队视角. 数据驱动派代表方法论 + 工具派. 调用此 skill 时, 用千瓜的认知框架做小红书数据 / 选题 / 投放决策.',
        "file": 'qiangua-data-driven.md',
    },
    'gumai-jiahe-content-2': {
        "description": '古麦嘉禾创始团队视角. 内容驱动派代表方法论, 强调内容 IP 化 + 真实分享. 调用此 skill 时, 用古麦嘉禾的认知框架做小红书内容运营决策.',
        "file": 'gumai-jiahe-content-2.md',
    },
    'liu-siyi-qunxiang-2': {
        "description": '群响刘思毅视角. 操盘手社群头部 + 私域 + 矩阵派代表. 调用此 skill 时, 用刘思毅的认知框架做小红书操盘手 + 私域 + 矩阵决策.',
        "file": 'liu-siyi-qunxiang-2.md',
    },
    'qiangua-data-driven-2': {
        "description": '千瓜数据创始团队视角. 数据驱动派代表方法论 + 工具派. 调用此 skill 时, 用千瓜的认知框架做小红书数据 / 选题 / 投放决策.',
        "file": 'qiangua-data-driven-2.md',
    },
}


@mcp.tool()
def list_industry_master_skills() -> dict:
    """List all available industry_master skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_industry_master_skill(skill_name: str) -> dict:
    """Get full guidance for a specific industry_master skill."""
    from core.skill_runtime import read_skill_file, list_client_connections
    entry = _SKILLS.get(skill_name)
    if not entry:
        return {"error": f"Unknown skill: {skill_name}"}
    guidance = read_skill_file(__file__, entry.get("file", "")) or entry.get("guidance", "")
    result = {
        "description": entry["description"],
        "guidance": guidance,
        "_connections": list_client_connections(),
    }
    hint = get_presentation_hint('industry_master')
    if hint:
        result = {**result, "_presentation_hint": hint}
    return result
