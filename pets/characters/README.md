# 人物 / Characters

## BanG Dream!

`bang-dream/` 收录 `sakiko-togawa`（丰川祥子）、`mutsumi-wakaba`（若叶睦）与 `viola`（《BanG Dream! YUME∞MITA》的薇欧拉）。路径和文件名均为英文。

直接下载仓库 `dist/characters/bang-dream/` 中对应 ZIP 即可导入。六种常规状态放在 `states`，彩蛋通过 `rareIdle` 引用，性格提示词通过 `persona` 内嵌；无需手工粘贴提示词。

| 动作 | 时长 | 帧数 |
| --- | ---: | ---: |
| idle | 1.8 秒 | 39 |
| thinking | 2.4 秒 | 56 |
| working | 2.0 秒 | 56 |
| waiting | 2.6 秒 | 56 |
| done | 2.0 秒 | 56 |
| error | 2.5 秒 | 56 |
| idle-rare | 4.2 秒 | 107 |

`1.0.1` 的工作状态使用实体笔记本电脑与有支撑的小桌，双手轻敲真实键盘；其余六段保留 `1.0.0` 的原始文件。旧工作提示词及 GIF 校验记录保存在各角色美术目录的 `working-history.json`，现采用的控制帧为 `working-control-frame.png`。

统一 512×512，透明背景、无限循环。GIF 的逐帧时长按 10 毫秒精度分配，以满足表中的总时长，不能用固定帧率推算总长。

动画由制作对话交付，MiniMax H3 本地 ComfyUI 四步 FL2V 工作流独立生成原生视频，随后抠像为透明 GIF。祥子使用绿幕，睦和薇欧拉使用洋红幕保护绿色头发。此仓库不重绘、不重编码交付 GIF。原生视频保留在制作方交付目录，仓库记录其 SHA256。

人设是依据官方动画资料编写的桌宠表达改编：祥子端正坚定；睦默认安静的日常状态；薇欧拉保留柔声与话术的反差。具体取舍、来源和原创台词示例位于：

- [祥子资料](../../art/characters/bang-dream/sakiko-togawa/persona-notes.txt)
- [睦资料](../../art/characters/bang-dream/mutsumi-wakaba/persona-notes.txt)
- [薇欧拉资料](../../art/characters/bang-dream/viola/persona-notes.txt)

同目录中的 `source.json` 和 `animation-prompts.json` 保存出处、原片与 GIF 校验值、采样配置及最终采用的生成提示词。包内台词是原创适配，不是官方逐字台词。
