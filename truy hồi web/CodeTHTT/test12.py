from whoosh.index import create_in
from whoosh.fields import   *
import os

schema=Schema(title=TEXT(stored=True),path=ID(stored=True),content=TEXT)
if not os.path.exists("index"):
  os.mkdir("index")
ix=create_in("index",schema)
writer = ix.writer()
writer.add_document(title="First document", path="/a",
content="This is the first document we've added!")
writer.add_document(title="Second document", path="/b",
content="The second one is even more interesting!")
writer.commit()
from whoosh.qparser import QueryParser
with ix.searcher() as searcher:
  query = QueryParser("title", ix.schema).parse("document")
  results = searcher.search(query)
  print(results[0])
