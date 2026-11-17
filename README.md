# Codex Lunaria Pet

An unofficial native Codex desktop Pets v2 package for Lunaria, a white-and-lavender dragon girl companion.

![Lunaria in several poses](preview.png)

## Install

Download this repository and open a terminal in the extracted folder. With Python 3.9 or later installed, run:

```sh
python3 install.py
```

The installer uses `$CODEX_HOME/pets/lunaria`, or `~/.codex/pets/lunaria` when `CODEX_HOME` is unset or empty. It copies only the metadata and sprite sheet. Running it again with identical files is harmless; if an existing pet has different files, it stops and asks you to back up and move that folder aside first. It does not change your selected pet.

For a manual installation, copy `pet.json` and `spritesheet.webp` into that same folder, preserving any existing customizations before replacing files. No Python runtime is needed to use the pet itself.

Then open Codex Desktop → Settings → Pets, refresh, and select Lunaria. Once the pet appears, you can adjust its size under Pets → Customize.

## Package contract

- `spriteVersionNumber`: `2`
- Spritesheet: 1536 × 2288 RGBA WebP
- Grid: 8 columns × 11 rows
- Cell size: 192 × 208 pixels
- The sheet contains the required state and look-direction frames used by native Pets.

## Files

- `install.py` — dependency-free installer that preserves existing customizations
- `pet.json` — native Pets metadata and sprite-sheet configuration
- `spritesheet.webp` — transparent animated sprite sheet
- `preview.png` — a few frames from the sheet, for this README
- `ARTWORK-NOTICE.md` — artwork and attribution scope
- `LICENSE` — MIT license for the package metadata and documentation

## Verify changes

```sh
python3 -m unittest discover -s tests -v
```

The tests use temporary directories and do not touch your installed pets. They cover default and custom destinations, repeat installs, preserving modified files, and invalid metadata.

## Scope

This is a fan-made package and is not affiliated with, endorsed by, or sponsored by OpenAI or Codex. See `ARTWORK-NOTICE.md` before redistributing artwork.

## Build cost

This package was vibe-coded with OpenAI Codex. Usage was not recorded, so this is a rough **estimate**, not a measurement:

| | Approx. |
| --- | --- |
| Tokens processed | ~3M–15M (mostly cached context re-reads) |
| Image generation | not included |

The text work is small (a metadata file and assembling 88 frames into a sheet that matches the Pets v2 grid), but fitting the frames to the grid usually takes several rounds of scripted image processing. Generating the artwork itself is billed separately and is not counted here. The range is scaled from a measured session of similar size ([Clay](https://github.com/junyii37/markdown-viewer-themes): ~11M tokens processed).
