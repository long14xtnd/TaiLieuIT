import os
for dirname, _, filenames in os.walk('C:\Users\Admin\Desktop\tài liệu\khai phá dữ liệu\See_Data.csv'):
    for filename in filenames:
        print(os.path.join(dirname, filename))