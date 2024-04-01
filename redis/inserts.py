import json
import random

with open('data.json') as f:
    data = json.load(f)


with open("string-inserts.txt", "w") as out:
    i = 0
    for obj in data:
        for k in obj.keys():
            out.write(f"set string:{i}:{k} {json.dumps(obj[k])}\n")
        i += 1

with open("hashtable-inserts.txt", "w") as out:
    i = 0
    for obj in data:
        for k in obj.keys():
            out.write(f"hset hashtable:{i} {k} {json.dumps(obj[k])}\n")
        i += 1


with open("list-inserts.txt", "w") as out:
    i = 0
    for obj in data:
        for k in obj.keys():
            out.write(f"rpush list:{i} {k}:{json.dumps(obj[k])}\n")
        i += 1

with open("zset-inserts.txt", "w") as out:
    i = 0
    for obj in data:
        for k in obj.keys():
            out.write(f"zadd zset:{i} {random.randint(0, 100)} {k}:{json.dumps(obj[k])}\n")
        i += 1