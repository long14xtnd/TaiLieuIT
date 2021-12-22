print ("yêu em!")
a,b,c = 12,13,14
d = 20

print (type(d))
print (hex(a))

floatA = float(d)
print (floatA)
print ("nội dung 1", "- nội dung 2")
print("Hihi \"haha\" ")
print("Hihi \t hihi")

#binding chuỗi
a1 = "Ban"
hi = "yêu e"
d1 = 20
all = " %s đến   %s %i lần" %(a1,hi,d1)
print(all)
print(5//2)

hihi =["Vu Dinh Phu", 1851171556, "60PM1", "09/05/2000"]
print(hihi[0])  # ket qua: Vu Dinh Phu
print(hihi[1])  #ket uqa 1851171556
print(hihi[-2])  #kqua: 60PM1
print(hihi[0:2])  #Vu Dinh Phu, 1851171556

#sửa phần tử trong list
hihi[1] = 25
print(hihi)

# xóa phần tử trong list
del hihi[1] # xoa phafn tuw 1
print(hihi)

# 2 list lồng nhau
list1 = ["abc",123, "def"]
print(hihi  + list1)

list1 = [9,5,2000]
list2 = ['vu dinh phu', list1]
print(list2)

chuoi1 = list2[1]   # [9,5,2000]
chuoi2 = list2[0]   # vu dinh phu
print(chuoi1)       #9,5,2000
print(chuoi2[0:2]) # vu

# tuple
tup_le = ("123",456,"789",101112,"hihi")
tup_le1 = ("aaaaaaa","bbbbb",tup_le)
print(tup_le1)
print(tup_le1[2][1])


