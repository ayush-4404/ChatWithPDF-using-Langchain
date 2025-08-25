# ChatWithPDF using Langchain

ChatWithPDF-using-Langchain is a web application that allows users to chat with PDF documents using natural language queries. Built with LangChain, this project leverages modern NLP techniques to enable users to extract information, summarize content, and interact conversationally with the contents of any PDF.

## Features

- **PDF Upload:** Easily upload your PDF documents.
- **Conversational AI:** Ask questions and get answers extracted from your PDF.
- **Summarization:** Get summaries of your PDF sections or the whole document.
- **Contextual Search:** Retrieve relevant information based on your queries.
- **Intuitive Interface:** Simple and user-friendly web interface.

## Tech Stack

- **Backend:** [LangChain](https://github.com/hwchase17/langchain), FastAPI
- **Frontend:** Streamlit (or your chosen UI framework)
- **PDF Parsing:** PyPDF2 / PDFPlumber
- **Embeddings/LLM:** OpenAI API or any supported LLM provider

## Getting Started

### Prerequisites

- Python 3.8+
- [OpenAI API Key](https://platform.openai.com/account/api-keys) (or any supported LLM provider key)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ayush-4404/ChatWithPDF-using-Langchain.git
   cd ChatWithPDF-using-Langchain
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set your API keys:**

   Create a `.env` file in the project root and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. **Run the application:**
   - For Streamlit:
     ```bash
     streamlit run app.py
     ```
   - For FastAPI:
     ```bash
     uvicorn main:app --reload
     ```

## Usage

- Upload a PDF via the web UI.
- Type your questions in natural language (e.g., "Summarize section 2", "What is the main topic of this document?").
- The app will process your query using LangChain and return results based on the PDF content.

## Project Structure

```
.
├── app.py                # Main Streamlit app (UI)
├── main.py               # FastAPI backend (if applicable)
├── pdf_utils.py          # PDF parsing utilities
├── langchain_utils.py    # LangChain integration utilities
├── requirements.txt
└── README.md
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for bug fixes, improvements, or new features.

## License

This project is licensed under the MIT License.

## Acknowledgements

- [LangChain](https://github.com/hwchase17/langchain)
- [OpenAI](https://openai.com/)
- [Streamlit](https://streamlit.io/)
- [PyPDF2](https://github.com/py-pdf/PyPDF2)

---

**Happy Chatting with your PDFs!**
