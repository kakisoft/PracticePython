from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry が到着
queue.append("Graham")          # Graham が到着
print(queue.popleft())                # 最初に到着した人が去って行った

print(queue)

queue.popleft()                 # 2番目の人も去って行った

queue                           # キューに残っているものは到着順
print(queue)

