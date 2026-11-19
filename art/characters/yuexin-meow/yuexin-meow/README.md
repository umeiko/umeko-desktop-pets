# Yuexin Meow / 月薪喵

2026-11-19 验收的七段桌宠动画，角色来自创作者“月薪喵”的简笔布偶猫形象。本包属于非官方桌宠改编；原角色权利归创作者，台词和工作助手人设为本项目适配。

- 作者介绍：https://www.sina.cn/news/detail/5205405028059490.html
- `character.png` 与 `working-reference.png` 是本轮生成的唯一中性和工作参考图。`reference/references/` 保留作者参考来源及校验记录，`reference/` 是交付使用的原输入包。
- `prompts/` 是真正送入模型的最终文本，`source-prompts/` 是最初定稿，`all-submitted-text.json` 记录编码器 Picture 标签及空负向条件，`workflows/` 保存每段真实请求和历史。
- `native/` 保留 MiniMax H3 FL2VA + LightX2V v1.2 四步原生 24fps 视频。透明由绿幕 CPU 抠像获得，非模型原生 alpha；所有实际正序帧保留，GIF 未在资源仓库重编码。
- `source.json` 记录原片、参考图及七个 GIF 的 SHA256。`delivery-SHA256SUMS.txt` 是制作方原始交付布局的校验清单，GIF 原字节位于对应 `pets/characters/yuexin-meow/yuexin-meow/`；其他记录保留在本目录。
- `validation.json` 记录多帧/时长/透明、实际宿主导入和 Python 播放结果。`acceptance.json` 保存用户“挺不错”“上传pet仓吧”的验收与上传授权。

工作状态的实体笔记本与带支撑桌脚的小桌贯穿整段，猫爪接触键盘。思考实际使用双爪在下巴下方，出错是双爪胸脸侧挤眼，工作有两次眨眼，完成有小张嘴。稀有待机采用内容修订 r2：一爪掩鼻，另一爪外展后在胸前小幅扇动，实际不是精确两次等幅扇动。这些差异已在用户验收前记录。旧 r1 拒收证据保留在原制作项目，未混入发布包。
