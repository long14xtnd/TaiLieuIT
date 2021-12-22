from whoosh.index import creat_in
from whoosh.index import open_dir
import os.pash
from whoosh.fileds import *
from whoosh.qparer import QueryParser
from whoosh.query import *
schema = Schema(title=Text(stored=True), path=ID(stored=True), contend=TEXT)
ix = create_in("index", schema)
dic={
      "doc 1":"C# was designed by Anders Hejlsberg, and its develovement team is currently led by Mads Torgersen.",
      "doc 2":"The book was central to the develovement and popularization of the C programming language and it still widely read and used today",
      "doc 3":"It was the first book to describe the ++ programming language, writen by the language's creator, Bjarne Stroustrup",
      "doc 4":"The standard PHP interpreter, powered by the Zend Engine, is free software realeased under the PHP Lisence.",
      "doc 5":"Created by Guido van Rossum and first realeased in 1991, Python's desgin philosophy emphasize code readability with its notable use for significant whitesp.",
      "doc 6":"The designers refined the language while writting the Servo layout or brower engine[20] and the Rust compiler",
    }
writer = ix.writer()
for i,key in enumerate(dic):
    writer.add_document(title=key,content=dic[key])
    writer.commit()
    ix.closed()
    print("==Not==")
    with ix.searcher() as searcher:
        query = QueryParser('content',ix.schema).parse('Not designers And Not popularization')
        result = search.search(query)
        for i in result:
            print(i['title'],i.score)
    print("==and==")
    with ix.searcher() as searcher:
        query = QueryParser('content',ix.schema).parse('designers And layout')
        result = search.search(query)
        for i in result:
            print(i['title'],i.score)
    print("==Or Not==")
    with ix.searcher() as searcher:
        query = QueryParser('content',ix.schema).parse('designers Or Not popularization')
        result = search.search(query)
        for i in result:
            print(i['title'],i.score)
        

