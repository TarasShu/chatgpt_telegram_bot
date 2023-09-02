import config
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone



class VectorData:
        
        pinecone_api_key = "9563d5a7-04cc-49ff-8f96-e44dc4b7fe44"
        index_name="ole-data"
        pinecone.init(api_key=pinecone_api_key,
                        environment="gcp-starter")
        index = pinecone.Index(index_name)


        print(pinecone.list_indexes())
        print(index.describe_index_stats())


