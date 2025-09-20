import heapq
class TaskManager:

    def __init__(self, tasks: list[list[int]]):
        self._tasks = []
        self._taskid_map = {}  # taskId -> (priority, userId)
        for userId, taskId, priority in tasks:
            heapq.heappush(self._tasks, (-priority, -taskId, userId))  # (-prio,-taskId,userId)
            self._taskid_map[taskId] = (priority, userId)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        heapq.heappush(self._tasks, (-priority, -taskId, userId))
        self._taskid_map[taskId] = (priority, userId)

    def edit(self, taskId: int, newPriority: int) -> None:
        usrid = self._taskid_map[taskId][1]
        self.rmv(taskId)
        self.add(usrid, taskId, newPriority)

    def rmv(self, taskId: int) -> None:
        del self._taskid_map[taskId]  # lazy del

    def execTop(self) -> int:
        while self._tasks:
            prio, neg_taskId, usrid = heapq.heappop(self._tasks)
            taskId = -neg_taskId
            if taskId in self._taskid_map and self._taskid_map[taskId] == (-prio, usrid):
                del self._taskid_map[taskId]
                return usrid
        return -1
