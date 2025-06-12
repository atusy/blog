import asyncio
import json
import sys

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_ollama import ChatOllama
from pydantic import BaseModel, Field


class X(BaseModel):
    name: str = Field(...)
    birthplace: str = Field(...)


async def construct_x(client: ChatOllama, system_prompt: str, user_prompt: str) -> X:
    _ = SystemMessage
    result = await client.with_structured_output(X).ainvoke(
        [SystemMessage(content=system_prompt), HumanMessage(content=user_prompt)]
    )

    if not isinstance(result, X):
        raise TypeError

    print(json.dumps(result.model_dump(), ensure_ascii=False))


async def main():
    _, model, system_prompt, user_prompt = sys.argv
    client = ChatOllama(model=model, temperature=0)

    await asyncio.gather(
        *[construct_x(client, system_prompt, user_prompt) for _ in range(10)]
    )


asyncio.run(main())
