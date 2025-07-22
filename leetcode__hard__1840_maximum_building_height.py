class Solution:
    def maxBuilding(self, n: int, res: List[List[int]]) -> int:
        maxhi = [i for i in range(n)]
        for i, h in res:
            maxhi[i-1] = h
        thish = 0
        for i in range(n):
            thish = min(maxhi[i], thish)
            maxhi[i] = thish
            thish += 1
        thish = maxhi[-1]
        maxh = maxhi[-1]
        for i in range(n-1, -1, -1):
            thish = min(maxhi[i], thish)
            maxhi[i] = thish
            if thish > maxh: maxh = thish
            thish += 1
        return maxh


class Solution:
    def getMaxCross(self, c1, c2):
        cross_x = (c1[0] - c1[1] + c2[0] + c2[1]) // 2
        cross_y = cross_x - c1[0] + c1[1]
        c1max_y = c1[1] + c2[0] - c1[0]
        c2max_y = c2[1] + c2[0] - c1[0]
        cords = [[c1[0], c2max_y, 0], [cross_x, cross_y, 1], [c2[0], c1max_y, 2]]
        cords.sort(key=lambda x: x[1])
        return cords[0]

    def maxBuilding(self, n: int, res: List[List[int]]) -> int:
        res.append([1, 0])
        res.sort()
        print(res)
        maxhq = deque([0])
        cross_type = 0
        for cord1, cord2 in zip(res, res[1:]):
            if cross_type == 2: cord1 = x, h
            x, h, cross_type = self.getMaxCross(cord1, cord2)
            print(f"{cord1}, {cord2} -> {h}")
            if cross_type == 0:
                maxhq.pop()
                maxhq
            if cross_type != 2 and h > maxhq[-1]: maxhq.append(h)
        a, b = res[-1]
        h = b + n - a
        if h > maxh: maxh = h
        return maxh

class Solution:
    def getCross(self, c1, c2):
        cross_x = (c1[0] - c1[1] + c2[0] + c2[1]) // 2
        cross_y = cross_x - c1[0] + c1[1]
        return cross_y
    
    def maxBuilding(self, n: int, res: List[List[int]]) -> int:
        res.append([1, 0])
        res.sort()
        res.append([n, res[-1][1] + n - res[-1][0]])
        hs = [0] * len(res)
        for i in range(1, len(res)):
            hs[i] = min(hs[i-1] + res[i][0] - res[i-1][0], res[i][1])
        for i in range(len(res)-2, -1, -1):
            hs[i] = max(min(hs[i], min(hs[i+1] + res[i+1][0] - res[i][0], res[i][1])), self.getCross(res[i-1], res[i]))
        return max(hs)


# last
class Solution:
    def getCross(self, c1, c2):
        cross_x = (c1[0] - c1[1] + c2[0] + c2[1]) // 2
        cross_y = cross_x - c1[0] + c1[1]
        return cross_x, cross_y

    def maxBuilding(self, n: int, res: List[List[int]]) -> int:
        res.append([1, 0])
        res.sort()
        res.append([n, res[-1][1] + n - res[-1][0]])
        for i in range(1, len(res)):
            res[i][1] = min(res[i-1][1] + res[i][0] - res[i-1][0], res[i][1])
        for i in range(len(res)-2, -1, -1):
            res[i][1] = min(res[i][1], min(res[i+1][1] + res[i+1][0] - res[i][0], res[i][1]))
        
        for i in range(len(res)-1):
            res.append(self.getMaxCross(res[i], res[i+1]))
            
        return max(res, key=lambda x: x[1])[1]