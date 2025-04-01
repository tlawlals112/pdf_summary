from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.llms import Ollama
from langchain.chains.summarize import load_summarize_chain

# 1. PDF 로드
loader = PyMuPDFLoader("0x03-AccessControl.pdf")
docs = loader.load()

# 2. 분할
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
chunks = splitter.split_documents(docs)

# 3. 로컬 모델 연결 (mistral 모델)
llm = Ollama(model="mistral")

# 4. 요약 체인 구성 및 실행
summary_chain = load_summarize_chain(llm, chain_type="stuff")
summary = summary_chain.invoke({"input_documents": chunks[:5]})  # 요약 범위 제한 가능
print(summary["output_text"])


