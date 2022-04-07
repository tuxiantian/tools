# coding:utf-8
# 添加PDF书签
from util import MyPDFHandler, PDFHandleMode as mode


def main():
    pdf_handler = MyPDFHandler(u'Python实战案例合集.pdf', mode=mode.NEWLY)
    pdf_handler.add_bookmarks_by_read_txt('title.txt', page_offset=0)
    pdf_handler.save2file(u'Python实战案例合集2.pdf')


if __name__ == '__main__':
    main()
