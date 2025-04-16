import langchain_core
from langchain_core.messages import HumanMessage
from langchain_google_vertexai import ChatVertexAI

if langchain_core.__version__ >= "0.3":
    from pydantic import BaseModel, Field
else:
    from langchain_core.pydantic_v1 import BaseModel, Field


class Data(BaseModel):
    x: str = Field()


def main():
    for model_name in [
        "gemini-1.5-pro-002",
        "gemini-2.0-flash-001",
    ]:
        print(model_name)
        llm = ChatVertexAI(
            model_name=model_name,
            temperature=0.0,
            max_tokens=8192,
            location="us-central1",
        )

        message = "x: x"

        for i in range(5):
            content = llm.with_structured_output(Data).invoke(
                [HumanMessage(content=[{"type": "text", "text": message}])]
            )
            print(content)


main()
