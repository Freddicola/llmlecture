from langchain_core.runnables import RunnableLambda
chain = RunnableLambda(lambda x: x)

from langsmith.schemas import Run, Example

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

def my_score_evaluator(run: Run, example: Example) -> dict:
    #   (run.outputs["result"], example.outputs["answer"])로부터 score를 계산
    # 실제 너무 어려운 작업이니까, LLM에 시킨다.
    import random
    return {"key": "my_score", "score": random.randint(1, 11)}   # 랜덤 평가

from langsmith.evaluation import evaluate, LangChainStringEvaluator

qa_evaluator = LangChainStringEvaluator("qa", config={"llm": llm})

# lang smith에서 제공하는 평가 도구를 사용하여 평가
experiment_results = evaluate(
    lambda inputs: {"result": chain.invoke(inputs["question"])},
    data="AGENT_DATASET",
    evaluators=[my_score_evaluator],
    experiment_prefix="RAG_EVAL",
)
