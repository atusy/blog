import asyncio
import json
import sys

from json_schema_to_pydantic import create_model
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_ollama import ChatOllama
from pydantic import BaseModel


async def construct_x(client: ChatOllama, user_prompt: str, model: type[BaseModel]):
    _ = SystemMessage
    result = await client.with_structured_output(model).ainvoke(
        [
            SystemMessage(content="入力に忠実に構造化出力して"),
            HumanMessage(content=user_prompt),
        ]
    )

    if not isinstance(result, model):
        raise TypeError

    print(json.dumps(result.model_dump(), ensure_ascii=False))


async def main():
    _, llm, user_prompt, schema = sys.argv
    model = create_model(json.loads(schema))

    client = ChatOllama(model=llm, temperature=0)

    iterations = 5

    if llm.endswith(":1b") or llm.endswith(":4b"):
        await asyncio.gather(
            *[construct_x(client, user_prompt, model) for _ in range(iterations)]
        )
        return

    for _ in range(iterations):
        await construct_x(client, user_prompt, model)


asyncio.run(main())
