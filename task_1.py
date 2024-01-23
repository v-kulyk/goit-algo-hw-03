from pathlib import Path
import shutil
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--src", type=Path)
    parser.add_argument("--dst", type=Path, default="dist")
    return parser.parse_args()

def recursive_copy(src:Path, dst:Path):
    if not dst.exists():
        dst.mkdir(exist_ok=True, parents=True)

    for elem in src.iterdir():
        if elem.is_dir():
            recursive_copy(elem, dst / elem.name)
        else:
            extension = elem.suffix[1:]
            if not dst.joinpath(extension).exists():
                dst.joinpath(extension).mkdir(exist_ok=True, parents=True)
            shutil.copy(elem, dst / extension / elem.name)

def main():
    try:
        args = parse_args()
        recursive_copy(args.src, args.dst)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()