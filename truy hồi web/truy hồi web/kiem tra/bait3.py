import os
import math

T = "The C Programming Language read and used"
T=T.split(" ")  
Q="The C Programming"
Q=Q.split(" ")

def readfile():
  res={}
  for file in os.listdir("res/"): 
    if file.endswith(".txt"): 
      file_content=read_text("res/"+file) 
      res[file]=file_content
  return res
def read_text( file_path): 
  with open(file_path,"r") as file:
    content= file.read()
    content= content.split(" ")
    # print(content)
    return content

def Vector(d,t) :
  vector=[] 
  for t in T:
    vector.append(d.count(t)) 
  return vector


def normalize( vector):
  vectorlength=0
  normalizedVector=[]
  for v in vector:
    vectorlength+= v*2
  vectorlength=math.sqrt(vectorlength)
  for v in vector:
    normalizedVector.append(v/vectorlength)
  return normalizedVector
def simp(vectorq, vectord):
  dot=0
  for v in range(len(vectorq)):
    dot+= vectorq[v]*vectord[v]
  return dot

score ={}
D=readfile()
for d in D:
  content=D[d]
  score[d]=simp(Vector(content,T),Vector(Q,T))
print(score)
print(sorted(score.items() ,key = lambda x : x[1], reverse=True))
