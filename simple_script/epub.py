import ebooklib
from ebooklib import epub

book = epub.read_epub('./Infinite_Jest__David_Foster_Wallace.epub')

docname = "inf_jest"


print()
for item in book.get_items():
    if item.get_type() == ebooklib.ITEM_DOCUMENT:
        print('==================================')
        print('NAME : ', item.get_name())
        print('----------------------------------')
        # print(item.get_content())
        # with open(f"./{docname}/{item.get_name().split('/')[-1]}", "r") as f:
        #     print(f.read())
        #     # f.write(item.get_content())
        print('==================================')
