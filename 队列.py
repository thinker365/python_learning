import queue
# 后进先出 last in first out --->lifo
# q = queue.LifoQueue()
# q.put(1)
# q.put(2)
# q.put(3)
# print(q.get())
# print(q.get())
# print(q.get())
q = queue.PriorityQueue()
q.put((10, 'lly1'))
q.put((-1, 'lly2'))
q.put((9, 'lly3'))
q.put((7, 'lly4'))
print(q.get())
print(q.get())
print(q.get())
print(q.get())
