from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatAnthropic
from langchain_openai import ChatOpenAI
from langserve import add_routes


def create_app():
    app = FastAPI(
        title="LangChain Server",
        version="1.0",
        description="A simple api server using Langchain's Runnable interfaces",
    )
    add_routes(
        app,
        ChatOpenAI(),
        path="/openai",
    )
    add_routes(
        app,
        ChatAnthropic(),
        path="/anthropic",
    )
    model = ChatAnthropic()
    prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")
    add_routes(
        app,
        prompt | model,
        path="/joke",
    )
    return app


if __name__ == "__main__":
    import uvicorn
    from src.utils.util import load_secrets

    load_secrets()
    # /playground
    # /docs
    uvicorn.run(create_app(), host="localhost", port=8000)
