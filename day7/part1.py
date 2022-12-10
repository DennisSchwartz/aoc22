import copy
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Dict, List, Union


@dataclass
class File:
    name: str
    size: int


@dataclass
class Directory:
    parent_dir: 'Directory'
    name: str
    abs_path: List[str] = field(default_factory=list)
    contents: List = field(default_factory=dict)


def du(obj: Union[Directory, File]) -> int:
    if isinstance(obj, File):
        return obj.size
    if isinstance(obj, Directory):
        size = sum([du(c) for c in obj.contents.values()])
        print('/' + f'{"/".join(obj.abs_path)} ({size})')
        return size
    raise TypeError('Only Directory or File are supported')


def get_sizes(cwd: Directory, acc: Dict[str, int] = defaultdict(int)) -> Dict[str, int]:
    assert isinstance(cwd, Directory)
    acc[f'/{"/".join(cwd.abs_path)}'] = du(cwd)
    for c in cwd.contents.values():
        if isinstance(c, Directory):
            acc = get_sizes(c, acc)
    return acc


def tree(obj: Union[Directory, File], depth: int = 0) -> None:
    padding = '  ' * depth
    if isinstance(obj, Directory):
        print(f'{padding}- {obj.name} (dir)')
        for c in obj.contents.values():
            tree(c, depth=depth+1)
    if isinstance(obj, File):
        print(f'{padding}- {obj.name} (file, size={obj.size})')


def main(in_file):
    lines = in_file.readlines()
    cwd: Directory = Directory(name='root', parent_dir=None)

    for line in lines:
        if line.startswith("$"):
            tmp = line.split()
            cmd = tmp[1]
            if cmd == 'ls':
                continue
            if cmd == 'cd':
                if tmp[2] == '..':
                    cwd = cwd.parent_dir
                elif tmp[2] == '/':
                    while cwd.parent_dir is not None:
                        cwd = cwd.parent_dir
                else:
                    cwd = cwd.contents[tmp[2]]
        else:
            tmp = line.split()
            if tmp[0] == 'dir':
                cwd.contents[tmp[1]] = Directory(
                    name=tmp[1],
                    parent_dir=cwd,
                    abs_path=cwd.abs_path + [tmp[1]]
                )
            else:
                cwd.contents[tmp[1]] = File(name=tmp[1], size=int(tmp[0]))

    # Move to root
    while cwd.parent_dir is not None:
        cwd = cwd.parent_dir

    # tree(cwd)

    dir_sizes = get_sizes(cwd)
    t = [(s, n) for n, s in dir_sizes.items() if s <= 100000]
    return sum([x[0] for x in t])


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        size = main(f)
        print(size)
