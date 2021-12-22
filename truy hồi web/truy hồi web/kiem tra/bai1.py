file = open('file1.txt')
list_string = file.read().split(" ")
counting_list={}  
for word in list_string:
  if not word in counting_list: 
      counting_list[word]=1
  else:
    counting_list[word]+=1
file.close()
print(counting_list)
