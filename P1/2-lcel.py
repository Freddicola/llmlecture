from langchain_core.runnables import RunnableLambda

r = RunnableLambda(lambda x: x + 1)
result = r.invoke(1)
print(result)           # 2

r2 = RunnableLambda(lambda x: x ** 2)

result = r.batch([1, 2, 3])
print(result)           # [2, 3, 4]

from langchain_core.runnables import RunnableSequence, RunnableParallel

chain = RunnableParallel(inc=r, sq=r2)
result = chain.invoke(2)
print(result)           # 4 

chain = r | {"inc": r, "sq": r2}
result = chain.invoke(2)
print(result)           # {'inc': 3, 'sq': 4}
