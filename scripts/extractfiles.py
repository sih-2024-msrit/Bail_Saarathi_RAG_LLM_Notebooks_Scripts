# IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII

import sys
import os


server_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if server_dir not in sys.path:
    sys.path.append(server_dir)

from langchain.vectorstores import Chroma


from prettyPrint import *
from vectorLoading import *

# IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII

def extract_file_info_from_similar_text(text, vectorDB):

  # Create a dictionary to store the mapped documents
  mapped_docs = {}

  docs = vectorDB.similarity_search(text, k=15)
  print("Length of similar related documents fetched: ", len(docs))
  print("Content of the docs is as follows: ")

  print()
  pretty_print_docs(docs)
  print()
  for doc in docs:
    source_file = doc.metadata['source'] if 'source' in doc.metadata else None
    # Check if page_content is not None
    if doc.page_content:
      if source_file not in mapped_docs:
        mapped_docs[source_file] = {"content": doc.page_content, "page_number": doc.metadata['page']}
      else:
        mapped_docs[source_file]["content"] += "\n" + doc.page_content


  print(mapped_docs.keys())

  return mapped_docs