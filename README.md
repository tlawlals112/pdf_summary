# 🧠 PDF 요약기 (LangChain + Ollama)

이 프로젝트는 로컬에서 실행 가능한 **PDF 요약기**입니다.  
OpenAI API 없이, **무료 로컬 언어모델(Ollama + Mistral)**을 이용해 PDF 내용을 텍스트로 요약합니다.

LLM 실험을 로컬에서 해보고 싶은 개발자나,
**PDF를 학습 전에 빠르게 훑어보고 싶을 때** 아주 유용하게 활용할 수 있습니다.

---

## 📦 사용 기술

- [LangChain](https://github.com/langchain-ai/langchain)
- [Ollama](https://ollama.com/)
- [Mistral](https://ollama.com/library/mistral) (로컬 언어 모델)
- [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/) (PDF 텍스트 추출)

---

## 🚀 설치 방법

### 1. 프로젝트 클론

```bash
git clone https://github.com/tlawlals112/pdf_summary.git
cd pdf_summary/
```

### 2. 가상환경 설정 (선택)

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. 필수 패키지 설치

```bash
pip install -r requirements.txt
```

> 또는 수동 설치:

```bash
pip install langchain langchain-community langchain-core pymupdf
```

---

## 🧠 Ollama 설치 (macOS 기준)

```bash
brew install ollama
ollama serve   # 서버 실행 (필수)
```

---

## 🧪 사용 방법

1. 분석할 PDF 파일을 프로젝트 루트에 넣기
2. 아래 명령어 실행:

```bash
python3 pdf_lang.py
```

3. 요약 결과는 터미널에 출력되며, `summary_output.txt`로 저장됩니다.

---

## 📄 예제 결과

예시 PDF: `0x03-AccessControl.pdf`  
요약 결과: `summary_output.txt`

---

## 🔧 설정 커스터마이징

- `chunk_size`, `chunk_overlap` 조절로 요약 범위 설정
- `chunks[:5]` → `chunks` 전체로 변경하면 전체 요약됨
- Ollama 모델을 바꾸고 싶다면:

```python
llm = Ollama(model="llama2")  # or codellama, gemma, etc.
```

---

## 📃 라이선스

MIT License

---

## 🙌 기여

이 프로젝트는 로컬 AI 실험을 위한 오픈소스입니다.  
문제 제보, 개선 제안, PR 환영합니다!


