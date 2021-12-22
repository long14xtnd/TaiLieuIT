from whoosh.index import create_in,open_dir
from whoosh.fields import   *
import os
def readfile():
  res={}
  for file in os.listdir("Wiki Docs/"):
    if file.endswith(".txt"):
      file_content=read_text("Wiki Docs/"+file)
      res[file_content[0]]=file_content[1]
  return res
def read_text( file_path):
  with open(file_path,"r") as file:
    content= file.read()
    content= content.split("\n\n",maxsplit=1)
    return content
if not os.path.exists("index"):
  schema=Schema(title=TEXT(stored=True),content=TEXT)
  os.mkdir("index")
  ix=create_in("index",schema)
  writer = ix.writer()
  res=readfile()
  for title in res:
    writer.add_document(title=title,
    content=res[title])
  writer.commit()
  print("index created")
else:
  ix = open_dir("index")
  print("index opened")
from whoosh.qparser import QueryParser
with ix.searcher() as searcher:
  query = QueryParser("content", ix.schema).parse("termed" or "Javascript")
  results = searcher.search(query)
  print(results[0])
