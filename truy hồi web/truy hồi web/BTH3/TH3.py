import os
from whoosh.index import create_in # Tạo lược đồ có hai trường title và content:
from whoosh.fields import Schema, TEXT, ID # Tạo chỉ mục ngược trong thư mục index, có lược đồ schema:
from whoosh.qparser import QueryParser

# Whoosh là thư viện tìm kiếm (truy hồi thông tin).
# whoosh.fields.ID: Một dãy từ đơn nhất, không tách thành các từ đơn lẻ. Ví dụ:đường dẫn file, URL, ngày tháng...
# • whoosh.fields.STORED: Chỉ lưu trữ lại, không lập chỉ mục trên kiểu trường này. Hữu ích cho những thông tin kèm theo kết quả tìm kiếm.
# • whoosh.fields.TEXT: Văn bản thông thường, có hỗ trợ lưu thông tin vị trí từ để dùng trong tìm kiếm cụm từ.

schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)

if not os.path.exists("index"):
    os.mkdir("index")

ix = create_in("index", schema)
writer = ix.writer()
filepaths = [os.path.join('docs', fn) for fn in os.listdir('docs')]
print(filepaths)

for path in filepaths:
    fp = open(path, 'r')
    text = fp.read().split('\n', 1)
    writer.add_document(title=os.path.split(
        path)[1] + ' : ' + text[0], path=path, content=text[1])
    fp.close()
writer.commit()  # Phải gọi commit để kết thúc

print("Tìm các văn bản thỏa mãn")
str1 = input("chứa tất cả các từ này: ")
str2 = input("chứa ít nhất một trong các từ này: ").split(" ") 
_str2 = " OR ".join(str2) 
str3 = input("không chứa các từ này: ").split(" ")
_str3 = "NOT "+"("+" OR ".join(str3)+")"
str2 = " ".join(str2)
str3 = " ".join(str3)

query1 = QueryParser("content", ix.schema).parse(str1)   #content trường tìm kiếm ngầm định
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
