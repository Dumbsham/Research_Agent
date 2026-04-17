from langchain.agents import create_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from pydantic import SecretStr
from tools import web_search, scrape_url
from dotenv import load_dotenv
import os
import time

load_dotenv()

# model setup (Qwen via OpenRouter)
llm1 = ChatOpenAI(
    model="qwen/qwen3-32b",
    temperature=0,
    api_key=SecretStr(os.getenv("OPENROUTER_API_KEY") or ""),
    base_url="https://openrouter.ai/api/v1"
)

# 1st agent
def build_search_agent():
    return create_agent(
        model=llm1,
        tools=[web_search]
    )

# 2nd agent
def build_reader_agent():
    return create_agent(
        model=llm1,
        tools=[scrape_url]
    )

# writer chain
writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer. Write clear, structured and insightful reports."),
    ("human", """Write a detailed research report on the topic below.

Topic: {topic}

Research Gathered:
{research}

Structure the report as:
- Introduction
- Key Findings (minimum 3 well-explained points)
- Conclusion
- Sources (list all URLs found in the research)

Be detailed, factual and professional."""),
])

writer_chain = writer_prompt | llm1 | StrOutputParser()

# critic chain
critic_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a sharp and constructive research critic. Be honest and specific."),
    ("human", """Review the research report below and evaluate it strictly.

Report:
{report}

Respond in this exact format:

Score: X/10

Strengths:
- ...
- ...

Areas to Improve:
- ...
- ...

One line verdict:
..."""),
])

critic_chain = critic_prompt | llm1 | StrOutputParser()


# debug test
if __name__ == "__main__":
    try:
        response = llm1.invoke("hello")
        print(response.content)
        time.sleep(2)
    except Exception as e:
        print("Error:", e)