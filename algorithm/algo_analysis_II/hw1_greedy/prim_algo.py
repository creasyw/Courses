import os, re
import numpy as np
from collections import defaultdict
import itertools
import heapq
finder = re.compile("-?\d+")

# Priority Queue with operations of delete and add
pq = []  # list of entries arranged in a heap
entry_finder = {}  # mapping of tasks to entries
REMOVED = '<removed-task>'  # placeholder for a removed task
counter = itertools.count()  # unique sequence count


def add_task(task, priority=0):
    'Add a new task or update the priority of an existing task'
    if task in entry_finder:
        remove_task(task)
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heapq.heappush(pq, entry)


def remove_task(task):
    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED
    # return priority
    return entry[0]


def pop_task():
    'Remove and return the lowest priority task. Raise KeyError if empty.'
    while pq:
        priority, count, task = heapq.heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return [task, priority]
    raise KeyError('pop from an empty priority queue')


def update(task, priority):
    'update task if exists, or push task into pq'
    try:
        old_priority = remove_task(task)
        add_task(task, min(old_priority, priority))
    except KeyError:
        add_task(task, priority)


def prim(graph):
    count = 0
    length = len(graph)
    result = np.zeros((length, 3))
    result[0, 0] = 10
    [update(k[0], k[1]) for k in graph[result[0, 0]]]
    while count < length - 1:
        result[count, 1:] = pop_task()
        result[count + 1, 0] = result[count, 1]
        [update(k[0], k[1])
         for k in graph[result[count, 1]] if k[0] not in result[:, 0]]
        #print result[count]
        count += 1
    return sum(result[:, 2])


def main():
    candidates = defaultdict(list)
    with open(os.path.join(
        os.path.dirname(__file__), "edges.txt")) as datafile:
        datafile.readline()
        for row in datafile:
            temp = [int(k) for k in finder.findall(row)]
            if temp[0] in candidates:
                candidates[temp[0]].append(temp[1:])
            else:
                candidates[temp[0]] = [temp[1:]]
            if temp[1] in candidates:
                candidates[temp[1]].append([temp[0], temp[2]])
            else:
                candidates[temp[1]] = [[temp[0], temp[2]]]
    print int(prim(candidates))


if __name__ == "__main__":
    main()
