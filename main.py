from dotenv import load_dotenv

load_dotenv()


import torch
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
# from langchain.llms import LlamaCpp
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain


from langchain_google_genai import ChatGoogleGenerativeAI

from pathlib import Path




llm_answer_gen = ChatGoogleGenerativeAI(model="gemini-2.5-pro", temperature=0.7)



device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

path = Path("Sachin.pdf")
loader = PyPDFLoader(file_path=path)
data = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=200)
text_chunks = text_splitter.split_documents(data)


# Create vector database for answer generation
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2", model_kwargs={"device": device})

# Initialize vector store for answer generation
vector_store = Chroma.from_documents(text_chunks, embeddings)

# Initialize retrieval chain for answer generation
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

answer_gen_chain = ConversationalRetrievalChain.from_llm(llm=llm_answer_gen, retriever=vector_store.as_retriever(),
                                                         memory=memory)

while True:

    user_input = input("Enter a question: ")
    if user_input.lower() == 'q':
        break

    # Run question generation chain
    answers = answer_gen_chain.invoke({"question": user_input})

    print("Answer: ", answers["answer"])