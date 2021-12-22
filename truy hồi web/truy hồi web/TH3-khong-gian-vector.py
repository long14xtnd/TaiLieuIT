

import nltk
import math


# đầu ra là tf: số lần xuất hiện của mỗi từ trong T thuộc d
def vector01(T, d):
    tokens = nltk.word_tokenize(T)
    output = []
    for value in tokens:
        count = d.count(value)
        output.append(count)
    return output

# chuẩn hóa


def normalize(vt):
    sum = 0
    for i in vt:
        sum += i*i

    if(sum == 0):
        sum = 1

    mau = round(math.sqrt(sum), 2)

    normalizeVector = []
    for i in vt:
        value = round(i / mau, 2)
        normalizeVector.append(value)

    return normalizeVector

# tính cosin


def cosin(vt1, vt2):
    tu = 0
    mau1 = 0
    mau2 = 0
    for i in range(len(vt1)):
        tu += vt1[i] * vt2[i]
        mau1 += vt1[i] * vt1[i]
        mau2 += vt2[i] * vt2[i]

    mau = (math.sqrt(mau1) + math.sqrt(mau2))
    if(mau == 0):
        mau = 1
    result = round(tu / mau, 2)
    return result


# T = 'a b'
# d = 'a b a b b s'

# vt = vector(T, d)
# normalizeVector = normalize(vt)
# result = cosin(vt, normalizeVector)

# print(result)

docs = {
    "doc1": "The C Programming Language(sometimes termed K & R, after its authors' initials).",
    "doc2": "Programming Language the book was regarded by many to be the authoritative reference on C.",
    "doc3": "C  # [b] (pronounced C sharp) se the book was co-authored by the original lan ",
    "doc4": "Java is a general-purpose programming language  language that is class-based, "
}

T = 'Programming The'

obj = {}
for key in docs.keys():
    vt = vector01(T, docs[key])
    nm = normalize(vt)
    cs = cosin(vt, nm)
    obj.update({key: cs})

output = sorted(obj.items(), reverse=True)

print(output)
