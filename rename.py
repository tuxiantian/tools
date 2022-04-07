import argparse
import os


def get_parser():
    parser = argparse.ArgumentParser(description='工作目录中文件后缀名修改')
    parser.add_argument('--work_dir', metavar='work_dir', type=str, nargs=1, help='修改后缀名的文件目录')
    parser.add_argument('--old_ext', metavar='old_ext', type=str, nargs=1, help='原来的后缀')
    parser.add_argument('--new_ext', metavar='new_ext', type=str, nargs=1, help='新的后缀')
    return parser


def batch_rename(work_dir, old_ext, new_ext):
    for filename in os.listdir(work_dir):
        split_file = os.path.splitext(filename)
        file_ext = split_file[1]
        if old_ext == file_ext:
            newfile = split_file[0] + new_ext
            os.rename(os.path.join(work_dir, filename), os.path.join(work_dir, newfile))
    print('完成重命名')
    print(os.listdir(work_dir))


if __name__ == '__main__':
    '''
    运行示例 python rename.py --work_dir=D:/temp --old_ext=txt --new_ext=md
    '''
    parser = get_parser()
    args = vars(parser.parse_args())
    work_dir = args['work_dir'][0]
    old_ext = args['old_ext'][0]
    if old_ext[0] != '.':
        old_ext = '.' + old_ext
    new_ext = args['new_ext'][0]
    if new_ext[0] != '.':
        new_ext = '.' + new_ext

    batch_rename(work_dir, old_ext, new_ext)
