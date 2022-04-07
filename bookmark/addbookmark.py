# coding:utf-8
# 添加PDF书签
from util import MyPDFHandler, PDFHandleMode as mode
import argparse
import os


def get_parser():
    parser = argparse.ArgumentParser(description='工作目录中文件书签添加')
    parser.add_argument('--work_dir', metavar='work_dir', type=str, nargs=1, help='工作目录')
    parser.add_argument('--old_file', metavar='old_file', type=str, nargs=1, help='原来的文件')
    parser.add_argument('--new_file', metavar='new_file', type=str, nargs=1, help='添加书签的文件')
    return parser


def main():
    parser = get_parser()
    args = vars(parser.parse_args())
    work_dir = args['work_dir'][0]
    old_file = args['old_file'][0]
    new_file = args['new_file'][0]

    pdf_handler = MyPDFHandler(u'' + os.path.join(work_dir, old_file), mode=mode.NEWLY)
    pdf_handler.add_bookmarks_by_read_txt('title.txt', page_offset=0)
    pdf_handler.save2file(u'' + os.path.join(work_dir, new_file))


if __name__ == '__main__':
    """
    运行示例 python addbookmark.py --work_dir=bookmark --old_file=bookmark/Python实战案例合集.pdf  --new_file=bookmark/Python实战案例合集2.pdf  
    """
    main()
