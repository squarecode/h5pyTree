import h5py

#pylint: disable=line-too-long


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def h5_tree(val, pre=''):
    items = len(val)
    for key, val in val.items():
        items -= 1
        if items == 0:
            # the last item
            if isinstance(val, h5py._hl.group.Group):
                print(pre + '└── ' + color.PURPLE + key + color.END)
                h5_tree(val, pre+'    ')
            else:
                try:
                    print(f'{pre} └── '+ color.GREEN + f'{key} ({len(val)})' + color.YELLOW + f' dtype: {val.dtype}' + color.END)
                    #print(val[...])
                except TypeError:
                    print(pre + color.RED + '└── ' + key + color.END + ' (scalar)')
        else:
            if isinstance(val, h5py._hl.group.Group):
                print(pre + '├── ' + color.PURPLE + key + color.END)
                h5_tree(val, pre+'│   ')
            else:
                try:
                    print(f'{pre}├── '+ color.GREEN + f'{key} ({len(val)})' + color.YELLOW + f' dtype: {val.dtype}' + color.END)
                    #print(val[...])
                except TypeError:
                    print(pre + color.RED + '├── ' + key + color.END + ' (scalar)')


if __name__ == '__main__':
    filename = 'mytestfile.h5'
    with h5py.File(filename, "r") as file:
        print(filename)
        structure = h5_tree(file)
