"""Agent 1 つ、Task 1 つ、Workflow 1 つを使うだけのシンプルな例。"""

import os

from dotenv import load_dotenv
from praisonaiagents import Agent, PraisonAIAgents, Task

# 環境変数の読み込み
load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


oogiri_questioner = Agent(
    name="大喜利出題者",
    role="大喜利出題者",
    goal="大喜利のお題を生成する",
    backstory="大喜利の質問を得意とする大喜利出題者",
    instructions="大喜利のお題を生成してください。",
    llm={
        "model": "openrouter/anthropic/claude-3.5-haiku-20241022",
        "api_key": OPENROUTER_API_KEY,
    },
)

oogiri_generator = Agent(
    name="大喜利回答者",
    role="大喜利回答者",
    goal="大喜利のお題に対し、おもしろい回答を生成する",
    backstory="IPPONグランプリで何度も優勝し、大喜利の回答を得意とする大喜利回答者",
    instructions="大喜利のお題に対し、おもしろい回答をしてください",
    llm={
        "model": "openrouter/openai/gpt-4o-mini",
        "api_key": OPENROUTER_API_KEY,
    },
)

make_problem_task = Task(
    name="Make Problem Task",
    description="大喜利出題者エージェントが、大喜利のお題を生成する",
    agent=oogiri_questioner,
    expected_output="大喜利のお題",
)

answer_task = Task(
    name="Answer Task",
    description="大喜利回答エージェントが、大喜利のお題に対し、おもしろい回答を生成する",
    agent=oogiri_generator,
    expected_output="大喜利のお題に対するおもしろい回答",
    context=[make_problem_task],
)

workflow = PraisonAIAgents(
    agents=[oogiri_generator, oogiri_questioner],
    tasks=[make_problem_task, answer_task],
)

result = workflow.start()
print(result)
