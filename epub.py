# import ebooklib
import glob
from ebooklib import epub
import bs4


def get_book():
    book_opt_dict = {}
    print("Books:")
    for i, book in enumerate(glob.glob("./library/*.epub"), 1):
        # print(str(i), book.split("/")[-1])
        print(str(i) + ": " + book.split("/")[-1])
        # print(str(i) + "\t" + book.split("/")[-1])
        book_opt_dict[str(i)] = book

    while (book_indx := input("select a book: ")) not in book_opt_dict.keys():
        print("this is not a valid book index")
        book_indx = input("select a book: ")
    # print(book_opt_dict[book_indx])
    # return book_opt_dict[book_indx]
    book = epub.read_epub(book_opt_dict[book_indx])
    return book

    # docname = "inf_jest"


def select_chapter(book_obj):
    print("content:")
    i = 0
    content_dict = {}

    # for item in book_obj.get_items():
    #     if item.get_type() == ebooklib.ITEM_DOCUMENT:
    for item in book_obj.toc:
        i += 1
        print(f"{i}: {item.title}")
        content_dict[str(i)] = item.title

        # print('----------------------------------')
    while (chapter_index := input("select a chapter: ")) not in content_dict.keys():
        chapter_index = input("select a chapter: ")
    # return content_dict[chapter_index]
    return chapter_index
    # print(item.get_content())
    # with open(f"./{docname}/{item.get_name().split('/')[-1]}", "r") as f:
    #     print(f.read())
    #     # f.write(item.get_content())


def open_chapter(book_obj, chapter_index):
    chapter = book_obj.get_item_with_href(
        book_obj.toc[int(chapter_index)].href)
    chapter_content = chapter.get_content()
    soup = bs4.BeautifulSoup(chapter_content, 'html.parser')

    bigga_print_list = []
    for string in soup.strings:
        print_me = repr(string)[1:-1]
        print_me = print_me.replace("\n        ", " ")
        print_me = print_me.replace("         ", " ")
        print_me = print_me.replace("\\n", "")
        print("  " + print_me)


def main():
    book_obj = get_book()
    chapter_index = select_chapter(book_obj)
    open_chapter(book_obj, chapter_index)


if __name__ == "__main__":
    main()
