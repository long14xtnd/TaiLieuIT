import os
from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID

from whoosh.qparser import QueryParser


schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT(stored=True))

if not os.path.exists("index"):
    os.mkdir("index")

    # Tạo chỉ mục
ix = create_in("index", schema)
writer = ix.writer()

filepaths = [os.path.join('./docs/', fn) for fn in os.listdir('./docs/')]

for path in filepaths:
    # Mở file
    fp = open(path, 'r')
    # Đọc toàn bộ nội dung file rồi tách xâu dựa trên dấu xuống dòng đầu tiên. Dòng đầu tiên là tiêu đề, phần còn lại là nội dung.
    text = fp.read().split('\n', 1)
    # Tiêu đề trong chỉ mục gồm tên file và tiêu đề văn bản
    writer.add_document(title=os.path.split(
        path)[1] + ' : ' + text[0], path=path, content=text[1])
    # Đóng file
    fp.close()
writer.commit()
print("Tìm các văn bản thỏa mãn")
str1 = input("chứa tất cả các từ này: ")
str2 = input("chứa ít nhất một trong các từ này: ").split(" ")
_str2 = " OR ".join(str2)
str3 = input("không chứa các từ này: ").split(" ")
_str3 = "NOT "+"("+" OR ".join(str3)+")"
str2 = " ".join(str2)
str3 = " ".join(str3)

query1 = QueryParser("content", ix.schema).parse(str1) 
query2 = QueryParser("content", ix.schema).parse(_str2)
query3 = QueryParser("content", ix.schema).parse(_str3)


def docs(query, s, str):
    result = searcher.search(query)
    print(s + " \"%s\" là: %d " % (str, len(result)))
    if(len(result)) > 0:
        for i in range(len(result)):
            print(result[i]['title'])


with ix.searcher() as searcher:
    docs(query1, "Số văn bản chứa các từ", str1)
    docs(query2, "Số văn bản chứa ít nhất một trong các từ", str2)
    docs(query3, "Số văn bản không chứa các từ", str3)