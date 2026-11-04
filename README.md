# Umeko Desktop Pets

可直接导入 [Umeko Desktop](https://github.com/umeiko/umeko-desktop) 的桌宠资源。

## 动物

| 宠物 | 预览 | 下载 |
| --- | --- | --- |
| 拉布拉多 | ![拉布拉多](pets/animals/labrador/idle.webp) | [拉布拉多 ZIP](dist/animals/umeko-pet-labrador-1.0.0.zip) |
| 布偶猫 | ![布偶猫](pets/animals/ragdoll/idle.webp) | [布偶猫 ZIP](dist/animals/umeko-pet-ragdoll-1.0.0.zip) |

每只宠物提供待机、思考、工作、等待、完成、出错六种透明循环动画，以及点击、悬停、拖动和任务结果台词。统一 384×384 画布；使用实际绘制的姿态帧，不通过拉伸身体制造动作。

## 人物

预留分类，暂未收录。新增资源时在 `pets/characters/` 下整理。

## 导入

1. 下载上表中的单只宠物 ZIP，无需解压。
2. 在 Umeko 中打开 **设置 → Agent → 插件管理 → 桌面小宠物**。
3. 点击导入形象，选择 ZIP，再选中已导入的宠物。

资源使用 `format: umeko-pet`、`version: 1`，ZIP 根目录包含 `pet.json` 和六个 WebP；不含代码或远程依赖。每个包的校验值见 [SHA256SUMS](dist/SHA256SUMS)。重复导入相同 id 会被宿主拒绝；升级前可先删除旧的自定义形象。

## 预览与重新打包

用任意静态文件服务器打开 [交互预览](preview/index.html)，可以切换动作、查看浅色/深色背景并下载 ZIP。

```bash
python -m pip install -r requirements.txt
python scripts/build_packs.py
python -m http.server 43465 --bind 127.0.0.1
```

生成后用准备好 PySide6 的 Umeko Python 环境验证：

```bash
python scripts/validate_packs.py --desktop-source /path/to/umeko-desktop
```

验证会调用宿主原有的 `import_pack` 和 `QImageReader`，真实解压到临时目录，检查全部动画帧、透明度、循环与格式限制；不会修改用户的形象库。

`art/animals/*/atlas.png` 保存最终原画，制作方式和提示词见 [美术说明](art/README.md)。`catalog.json` 是本仓库的分类和下载索引，不会改变 Umeko 的导入协议。

已验证的导出环境为 Pillow 11.1.0 / libwebp 1.5.0；相同环境下重复导出的 ZIP 校验值一致。更换编码器版本后可能需要更新校验值。

本仓库原创资源与工具按 MIT 许可证提供。
