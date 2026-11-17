# Hatsune Miku · character-r3 / idle-r3

已获用户验收的公式服初音单待机版，包版本 `1.0.0`。仅 `idle` 已交付并通过验收；其余状态由客户端回退显示待机，无彩蛋动画。旧造型动作不在本次发布范围内。

- `character.png`、`character-prompt.txt`：新版设计及实际绘图提示词。
- `idle-prompt.txt`：本轮提供给制作会话的正向动作提示词。
- `production/`：原生视频、实际提交文本、工作流、透明处理和原始制作记录。原始 GIF 保存在仓库 `pets/characters/piapro/hatsune-miku/idle.gif`，与交付字节一致；没有在美术目录重复存储。
- `persona.txt`、`persona.json`、`dialogue.json`：内嵌到宠物包的人设与原创台词。
- `source.json`、`acceptance.json`、`validation/`：来源、最终人类验收和有限导入/播放检查。

视频由 MiniMax H3 参考图引导原生生成。原片 39 帧、24 fps、1.625 秒；GIF 保留全部正序帧，以 40/50 ms 帧延时组成 1.8 秒循环。透明背景来自蓝幕抠像与边缘处理，不是模型直接输出透明背景。GIF 未重新编码。

`production/SHA256SUMS.txt` 是原交付目录的校验清单；其中 `idle.gif` 对应上述宠物目录，`character.png` 对应本目录。制作时的 JSON 与播放报告保持原样，其中“待人类验收”描述是历史状态，后续验收以 `acceptance.json` 为准。

鲸鱼娘仅用于画风、比例与脸型参考，相关 MIT 许可见 `whale-girl-license.txt`。本角色与台词是非官方桌宠改编，不代表官方作品或背书。
