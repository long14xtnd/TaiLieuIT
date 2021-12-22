string = 'The Project Gutenberg EBook of Crime and Punishment, by Fyodor Dostoevsky'
str = string.split(" ")

count = {}
for i in str:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

for i in sorted(count, key=count.get, reverse=False):
    print(i, count[i])