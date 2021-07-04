import sys
from typing import List
from pathlib import Path
from subprocess import run as prun, PIPE


__doc__ = """Usage: python3 epub2mobi.py SOURCE [TARGET]

EPUB to MOBI script, support recursively build the target.

[TARGET] is optional. If SOURCE is a file, then it should be the output file with extension (maybe not .mobi). \
If SOURCE is a folder, then it should be a folder name which will be automatically created by script. \
Wisely, you should leave it empty.

If SOURCE and [TARGET] are files, then the script run just like pure ebook-convert program. \
Ensure you have specify the extension of SOURCE and [TARGET].

Also, if TARGET is specified, the script will throw error is TARGET already exists.

Flags:
  -h, --help        display this help and exit
  -v, --detail      show convert detail from ebook-convert
  --same-dir        if given, [TARGET] will be ignore and will not separate source and target

Author: iyume <iyumelive@gmail.com>"""


cwd = Path(__file__).resolve().parent
# the target must be in the same folder as the epub2mobi.py
## cwd = Path.cwd()
## the target must be in the same folder as where you run epub2mobi.py

argv = sys.argv[:]
argv.pop(0)
show_detail = False
same_dir = False

if len(argv) == 0 or '--help' in argv or '-h' in argv:
    print(__doc__)
    exit(0)

if '--detail' in argv or '-v' in argv:
    argv = [i for i in argv if i != '--detail' or i != '-v']
    show_detail = True

if '--same-dir' in argv:
    argv.remove('--same-dir')
    same_dir = True

source = Path(argv[0])

# TARGET not set
if source.is_file():
    target = source.with_suffix('.mobi')
elif source.is_dir():
    target = Path(str(Path(argv[0])) + '-build')
    target.mkdir(exist_ok=True)
    # if target.exists():
    #     raise RuntimeError(f'TargetExistsError: Target "{target}" already exist.')
else:
    raise RuntimeError(f'InputError: Source "{source}" is not a file or a folder or not exists.')

# TARGET set
if len(argv) > 1 and not same_dir:
    # ignore if set '--same-dir' flag
    target = Path(argv[1])
    if target.exists():
        raise RuntimeError(f'TargetExistsError: Target "{target}" already exist.')


def run_convert(input_file: Path, output_file: Path) -> None:
    if not input_file.is_file():
        raise RuntimeError('ConvertError: Parameter contains a path that is not a file.')
    result = prun(
        ['ebook-convert', input_file, output_file],
        stdout=PIPE,
        stderr=PIPE,
        encoding='utf-8')
    if result.returncode != 0:
        print(f'ConvertError: Please check parameter "{input_file}" and "{output_file}" is correct. '
                'Maybe source file has been damaged.')
        print()
        response = input('Do you want to continue? [Y/n] ')
        print()
        if response.lower() == 'y':
            ...
        else:
            print('Finished.')
            exit(0)
    if show_detail:
        print('* ' + result.stdout.strip('\n').replace('\n', '\n* '))


#run_convert(Path('./埃罗芒阿老师/埃罗芒阿老师 01 妹妹与不开之屋.ePub'), Path('./埃罗芒阿老师/埃罗芒阿老师 01 妹妹与不开之屋.mobi'))


def recurse_folder(path: Path) -> List[Path]:
    return sorted(path.glob('**/*.epub'))


#print(*[str(i) for i in recurse_folder(source)], sep='\n')


if source.is_file():
    print(f'Founded: {source}')
    print(f'Building {target}...')
    run_convert(source, target)
    print('Finished.')
    exit(0)

if source.is_dir():
    for epub_path in recurse_folder(source):
        mobi_path = target.joinpath(*epub_path.parts[len(source.parts):]).with_suffix('.mobi')
        # create sub folder
        mobi_path.parent.mkdir(parents=True, exist_ok=True)
        print(f'Founded: {epub_path}')
        print(f'Building {mobi_path}')
        run_convert(epub_path, mobi_path)
    print('Finished.')
    exit(0)
