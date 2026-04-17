# 🔬 ResearchMind — Multi-Agent AI Research Pipeline

> Four specialized AI agents collaborate to search, scrape, write, and critique — delivering a polished research report on any topic in seconds.

<br/>

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-0.2+-1C3C3C?style=flat-square&logo=langchain&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35+-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![OpenRouter](https://img.shields.io/badge/OpenRouter-Qwen3--32B-6B4FBB?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-22c55e?style=flat-square)

---

## What Is This?

ResearchMind is an **agentic AI pipeline** that automates the research process end-to-end. Instead of prompting a single LLM, it orchestrates four distinct agents, each with a focused role — mimicking how a real research team operates.

You give it a topic. It gives you a structured, sourced, and critically reviewed research report.

---

## Architecture

```
User Input
    │
    ▼
┌─────────────────┐
│  Search Agent   │  ← Tavily API: finds top 5 recent, reliable sources
└────────┬────────┘
         │
    ▼
┌─────────────────┐
│  Reader Agent   │  ← Scrapes the most relevant URL for deep content
└────────┬────────┘
         │
    ▼
┌─────────────────┐
│  Writer Chain   │  ← Drafts a full structured report (Intro → Findings → Conclusion)
└────────┬────────┘
         │
    ▼
┌─────────────────┐
│  Critic Chain   │  ← Scores the report and gives actionable feedback
└─────────────────┘
         │
    ▼
 Final Report + Critique
```

Each step feeds into the next. No shortcuts, no single-prompt magic — just a clean, inspectable pipeline.

---

## Features

- **Multi-agent orchestration** with LangChain's `create_agent`
- **Live web search** via [Tavily](https://tavily.com/) — not hallucinated, always current
- **URL scraping** with BeautifulSoup for deep content extraction
- **Structured report generation** with introduction, key findings, conclusion, and sources
- **Automated critic** that scores the report out of 10 and flags weaknesses
- **Streamlit UI** with real-time pipeline status indicators
- **Markdown download** of the final report
- **CLI mode** for terminal use without the UI

---

## Tech Stack

| Layer | Technology |
|---|---|
| LLM | Qwen3-32B via [OpenRouter](https://openrouter.ai) |
| Agent Framework | [LangChain](https://python.langchain.com/) |
| Web Search | [Tavily](https://tavily.com/) |
| Web Scraping | Requests + BeautifulSoup4 |
| UI | [Streamlit](https://streamlit.io/) |
| Env Management | python-dotenv |

---

## Quickstart

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/researchmind.git
cd researchmind
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up environment variables

Create a `.env` file in the project root:

```env
OPENROUTER_API_KEY=your_openrouter_key_here
TAVILY_API_KEY=your_tavily_key_here
```

- Get an OpenRouter key → [openrouter.ai/keys](https://openrouter.ai/keys)
- Get a Tavily key → [app.tavily.com](https://app.tavily.com/)

### 4. Run the app

**Streamlit UI:**
```bash
streamlit run app.py
```

**CLI mode:**
```bash
python pipeline.py
```

---

## Project Structure

```
researchmind/
├── app.py          # Streamlit frontend
├── agents.py       # Agent definitions, writer & critic chains
├── tools.py        # web_search and scrape_url tools
├── pipeline.py     # CLI pipeline runner
├── .env            # API keys (not committed)
├── requirements.txt
└── README.md
```

---

## Example Output

**Topic:** *"LLM agents 2025"*

The pipeline produces:

```
📝 Final Research Report
─────────────────────────
Introduction
  ...overview of the current LLM agent landscape...

Key Findings
  1. Tool use and function calling have become standard...
  2. Memory architectures are evolving rapidly...
  3. Multi-agent frameworks are seeing production adoption...

Conclusion
  ...

Sources
  - https://...
  - https://...

🧐 Critic Feedback
─────────────────────────
Score: 8/10

Strengths:
  - Well-structured and clearly written
  - Good sourcing with real URLs

Areas to Improve:
  - Could expand on limitations of current agent frameworks
  - Missing quantitative benchmarks

One line verdict:
  Solid, informative report — minor depth gaps in technical analysis.
```

---

## Configuration

You can swap the model by editing `agents.py`:

```python
llm1 = ChatOpenAI(
    model="qwen/qwen3-32b",  # ← change this to any OpenRouter model
    temperature=0,
    api_key=SecretStr(os.getenv("OPENROUTER_API_KEY")),
    base_url="https://openrouter.ai/api/v1"
)
```

Any model available on OpenRouter works here — `gpt-4o`, `claude-3.5-sonnet`, `mistral-large`, etc.

---

## Requirements

```
streamlit
langchain
langchain-openai
langchain-core
tavily-python
requests
beautifulsoup4
python-dotenv
pydantic
rich
```

---

## License

MIT — free to use, modify, and build on.

---

## Author

Built by **Saksham Sharma** · [GitHub](https://github.com/Dumbsham) · [LinkedIn](https://linkedin.com/in/saksham14sharma)

> *If this project helped you, consider giving it a ⭐ — it helps others find it.*
