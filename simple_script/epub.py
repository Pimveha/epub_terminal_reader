# import ebooklib
from ebooklib import epub
import bs4


def get_book():
    book = epub.read_epub('./Infinite_Jest__David_Foster_Wallace.epub')
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
    text = soup.get_text()
    print(text)
    # print(text.split("\n"))


def main():
    book_obj = get_book()
    chapter_index = select_chapter(book_obj)
    open_chapter(book_obj, chapter_index)


if __name__ == "__main__":
    main()
