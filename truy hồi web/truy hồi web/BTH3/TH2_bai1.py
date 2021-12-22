import nltk
from urllib import request
from bs4 import BeautifulSoup

nltk.download('popular')
raw = "mot hai ba bon nam sau mot hai nam chin"
tokens = nltk.word_tokenize(raw)

count = {}      
for i in tokens:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

print("văn bản raw")
for i in sorted(count, key=count.get):  
    print(i, count[i])
   



# k đc có 2 khóa trùng nhau
# Giá trị được lưu trong từ điển có thể thuộc bất kỳ kiểu nào trong khi khóa phải là kiểu bất biến như số, tuple hoặc chuỗi.
# Khóa sử dụng trong từ điển có phân biệt chữ hoa chữ thường

# Sử dụng %type để xác định kiểu biến
# len()  Trả về số lượng cặp trong từ điển
# cmp()  So sánh giá trị và khóa của hai từ điển
# Tuple có thể coi như tập hợp của các đối tượng bất biến trong Python.

# Sự khác biệt giữa danh sách (list) và tuple đó là danh sách được khai báo trong ngoặc vuông và có thể được thay đổi 
# trong khi tuple được khai báo trong ngoặc đơn và không thể thay đổi nhưng tupe duyêt nhanh hơn so với list

# lỗi: "indentation error: expected an indented block" là lỗi thò thụt đầu dòng 
# 4 dấu cách = 1 dấu tab
# for x in range (10,20):  lặp từ 10->19