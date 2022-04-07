import pdfplumber


def main():
    """
    提取一本书中的标题作为书签，输出到title.txt文件中
    """
    with open('title.txt', 'w', encoding='utf-8') as file:
        with pdfplumber.open('Python实战案例合集.pdf') as pdf:
            page_index: int = 1
            for page in pdf.pages:
                content = page.extract_text()
                rows = content.split('\n')
                for row in rows:
                    if row[0].isdigit():
                        file.write(row + '@' + str(page_index) + '\n')
                page_index += 1


if __name__ == '__main__':
    main()
