"""Agent 1 つ、Task 1 つ、Workflow 1 つを使うだけのシンプルな例。"""

import os

from dotenv import load_dotenv
from praisonaiagents import Agent, PraisonAIAgents, Task

# 環境変数の読み込み
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE")

oogiri_generator = Agent(
    name="大喜利回答者",
    role="大喜利回答者",
    goal="大喜利のお題に対し、おもしろい回答を生成する",
    backstory="IPPONグランプリで何度も優勝し、大喜利の回答を得意とする大喜利回答者",
    instructions="大喜利のお題に対し、おもしろい回答をしてください",
    llm={
        "model": "openai/gpt-4o-mini",
        "api_key": OPENAI_API_KEY,
        "api_base": OPENAI_API_BASE,
    },
)

answer_task = Task(
    name="Answer Task",
    description="大喜利回答エージェントが、大喜利のお題に対し、おもしろい回答を生成する",
    agent=oogiri_generator,
    expected_output="大喜利のお題に対するおもしろい回答",
)

workflow = PraisonAIAgents(
    agents=[oogiri_generator],
    tasks=[answer_task],
)

result = workflow.start("こんなAIはいやだ。どんなAI？")
print(result)
