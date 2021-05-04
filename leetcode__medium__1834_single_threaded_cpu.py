# https://leetcode.com/contest/weekly-contest-237/problems/single-threaded-cpu/
import heapq
from collections import deque


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, task in enumerate(tasks): task.append(i)  # [[et, pt, ind] ...]
        tasks = deque(sorted(tasks))  # at, pt, ind 각 각각 순서대로 작은 순
        
        clock, availables, order = 0, list(), list()
        while tasks or availables:
            while tasks and tasks[0][0] <= clock:
                _, pt, i = tasks.popleft()
                heapq.heappush(availables, ([pt, i], pt, i))  # heapq 가 맨 앞 원소를 기준으로 대소를 비교하기 때문
            if not availables and tasks: clock = tasks[0][0]  # cpu idle time
            else:
                clock += availables[0][1]  # processing time 반영
                order.append(heapq.heappop(availables)[2])  # index 저장
        return order