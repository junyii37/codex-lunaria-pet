# Codex Lunaria Pet

一个非官方的 Codex 原生桌面 Pets v2 角色包：Lunaria，一只白紫色、带角与龙翼的小龙少女。

This is an unofficial native Codex desktop Pets v2 package for Lunaria, a white-and-lavender dragon girl companion.

## 安装 / Install

将 `pet.json` 和 `spritesheet.webp` 放入 Codex 的自定义 Pets 目录：

```sh
mkdir -p "$CODEX_HOME/pets/lunaria"
cp pet.json spritesheet.webp "$CODEX_HOME/pets/lunaria/"
```

然后在 Codex Desktop 的 Settings → Pets 中刷新并选择 Lunaria。桌宠显示后，可通过 Pets 的 Customize 调整大小。

## Package contract

- `spriteVersionNumber`: `2`
- Spritesheet: 1536 × 2288 RGBA WebP
- Grid: 8 columns × 11 rows
- Cell size: 192 × 208 pixels
- The sheet contains the required state and look-direction frames used by native Pets.

## 文件 / Files

- `pet.json` — native Pets metadata and sprite-sheet configuration
- `spritesheet.webp` — transparent animated sprite sheet
- `ARTWORK-NOTICE.md` — artwork and attribution scope
- `LICENSE` — MIT license for the package metadata and documentation

## Scope

This is a fan-made package and is not affiliated with, endorsed by, or sponsored by OpenAI or Codex. See `ARTWORK-NOTICE.md` before redistributing artwork.
