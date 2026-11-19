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

## Hyouka / 冰菓

`hyouka/eru-chitanda/` 收录千反田爱瑠，路径和文件名均为英文。下载 [爱瑠 1.0.0 ZIP](../../dist/characters/hyouka/umeko-pet-eru-chitanda-1.0.0.zip) 即可导入；温柔、有礼、认真好奇的人设与原创互动台词已内嵌。

七段动画的帧数与总时长与上表一致，均为 512×512、透明背景、无限循环。工作状态从头到尾使用实体笔记本与有双腿支撑的小桌。原生 H3 四步 FL2V 视频独立生成，绿幕抠像后按目标时长分配 GIF 帧延迟，保留原生帧顺序；本仓库逐字节复制正式交付 GIF。

[爱瑠美术目录](../../art/characters/hyouka/eru-chitanda/) 保存两张设计图、实际控制帧、初始与最终提示词、人设及来源说明。`source.json` 和 `animation-prompts.json` 记录生成方法、原片与 GIF 的 SHA256；`validation.json` 记录多帧、透明、时长与实际宿主导入及 Python 播放结果。原生 MP4 留存在制作交付目录，不重复放入导入包。

## Piapro / 初音未来

`piapro/hatsune-miku/` 收录初音未来的公式服桌宠。[初音 1.0.0 ZIP](../../dist/characters/piapro/umeko-pet-hatsune-miku-1.0.0.zip) 是单待机版，仅含已验收的新造型 `idle.gif`：512×512、39 帧、1.8 秒、透明无限循环。其余状态由宿主回退到待机，不声明尚未制作的新造型动作或彩蛋。

原生 MiniMax H3 视频使用新参考图作为首尾控制图；蓝幕抠像后保留原生正序帧，GIF 每帧为 40 或 50 毫秒。包内 GIF 与正式交付 SHA256 一致。桌宠性格和互动台词是原创适配，并非官方逐字台词或唯一官方性格。

[初音美术目录](../../art/characters/piapro/hatsune-miku/) 保存新设计图、原始视频、实际模型提示词、工作流、透明处理及验收记录；原视频不放入导入 ZIP。旧造型动画与被否决的待机不在此包内。

## Yuexin Meow / 月薪喵

`yuexin-meow/yuexin-meow/` 收录月薪喵的简笔表情包造型。[月薪喵 1.0.0 ZIP](../../dist/characters/yuexin-meow/umeko-pet-yuexin-meow-1.0.0.zip) 已内嵌乐观、无厘头的工作陪伴人设与原创台词。

| 动作 | 时长 | 帧数 |
| --- | ---: | ---: |
| idle | 1.8 秒 | 39 |
| thinking | 2.4 秒 | 56 |
| working | 2.2 秒 | 56 |
| waiting | 2.4 秒 | 56 |
| done | 2.2 秒 | 56 |
| error | 2.4 秒 | 56 |
| idle-rare | 4.0 秒 | 107 |

统一 512×512，透明、无限循环。工作段全程保留实体笔记本和带两条支撑脚的小桌，稀有待机是一爪捂鼻、另一爪外展及胸前扇动。动画来自参考图引导的 MiniMax H3 FL2VA + LightX2V v1.2 四步原生视频，CPU 绿幕抠像后保留全部 426 个正序帧和交付 GIF 字节。透明是后期处理，蓝眼、白身和米棕色块保持实色。

[月薪喵美术目录](../../art/characters/yuexin-meow/yuexin-meow/) 保留作者参考、设计图、人设、原片、实际最终提示词、请求与工作流、制作侧动作差异说明及人类验收记录；原视频不放入导入 ZIP。
