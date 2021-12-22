fileptr = open('file1.txt')
somestring = fileptr.read()
couting_list={}
for char in somestring:
  if not char in couting_list: 
      couting_list[char]=1
  else:
    couting_list[char]+=1
print(couting_list)
fileptr.close()
