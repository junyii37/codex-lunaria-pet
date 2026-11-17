#!/usr/bin/env python3
"""Install Lunaria without overwriting an existing custom pet (Python 3.9+)."""
import json
import os
from pathlib import Path
import shutil
import tempfile

SOURCE = Path(__file__).resolve().parent
FILES = ('pet.json', 'spritesheet.webp')


def install(source=SOURCE, codex_home=None):
    source = Path(source)
    metadata = json.loads((source / 'pet.json').read_text(encoding='utf-8'))
    if (metadata.get('id'), metadata.get('spriteVersionNumber'), metadata.get('spritesheetPath')) != ('lunaria', 2, 'spritesheet.webp'):
        raise ValueError('Unexpected Lunaria metadata; installation cancelled.')
    # Check the image signature before creating anything in the destination.
    with (source / 'spritesheet.webp').open('rb') as image:
        header = image.read(12)
    if header[:4] != b'RIFF' or header[8:12] != b'WEBP':
        raise ValueError('The sprite sheet is not a WebP image.')
    home = Path(codex_home) if codex_home is not None else Path(os.environ.get('CODEX_HOME') or Path.home() / '.codex')
    pets = home.expanduser().resolve() / 'pets'
    target = pets / 'lunaria'
    if target.exists() or target.is_symlink():
        if not target.is_symlink() and all((target / name).is_file() and (target / name).read_bytes() == (source / name).read_bytes() for name in FILES):
            return target, False
        raise FileExistsError(f'{target} already exists with different files. Back it up and move it aside before installing.')
    pets.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix='.lunaria-', dir=pets))
    try:
        for name in FILES:
            shutil.copy2(source / name, staging / name)
        # mkdir reserves the name without ever replacing a concurrent install.
        target.mkdir()
        try:
            for name in FILES:
                shutil.move(str(staging / name), target / name)
        except BaseException:
            shutil.rmtree(target)
            raise
    finally:
        shutil.rmtree(staging)
    return target, True


if __name__ == '__main__':
    try:
        destination, changed = install()
        print(('Installed: ' if changed else 'Already installed: ') + str(destination))
        print('Refresh Pets in Codex Desktop, then select Lunaria.')
    except (OSError, ValueError) as error:
        raise SystemExit(str(error)) from error
