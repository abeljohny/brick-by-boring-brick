class Solution:
    def twoCitySchedCost(self, costs: list[list[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])
        n = len(costs) // 2
        return sum(cost[0] for cost in costs[:n]) + sum(cost[1] for cost in costs[n:])


print(Solution().twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]))
