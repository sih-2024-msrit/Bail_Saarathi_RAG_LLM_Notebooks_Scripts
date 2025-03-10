# IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
import sys
import os
# from langchain_chroma import Chroma

server_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if server_dir not in sys.path:
    sys.path.append(server_dir)
    
print(sys.path)

from vectorLoading import *
from crimekey import *
from ipcmap import *


def IPC_Sections_Charged(bail_applicant_crime_record_text, path_vector_store):

  # path_vector_store = "/content/drive/MyDrive/Bail_Saarathi/vector_database/New_IPC_Sections_VectorEmbeddings/"
  vectorDB = saved_vectorDB_loading(save_directory = path_vector_store)

  crimes_commited_list = crime_keywords_extraction(bail_applicant_crime_record_text)
  print(crimes_commited_list)

  crimes_to_ipc = map_IPC_sections(crimes_commited_list, vectorDB)
  print(crimes_to_ipc)

  return crimes_to_ipc

path_vector_store = "server/scripts/Bail_Saarathi/vector_database/IPC_Sections_VectorEmbeddings/"

bail_applicant_case_record_text = input("Case RECORD: ")

print(IPC_Sections_Charged(bail_applicant_case_record_text, path_vector_store))