# https://leetcode-cn.com/problems/meeting-rooms-ii/

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # intervals = []
        if not intervals:
            return 0
        
        free_rooms = []

        # 根据会议的开始时间排序
        intervals.sort(key=lambda x: x[0])

        heapq.heappush(free_rooms, intervals[0][1])

        for i in intervals[1:]:
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)

            heapq.heappush(free_rooms, i[1])

        return len(free_rooms)

        # >>> items = [1,2,9,7,3]
        # >>> heapq.heappush(items,10)
        # >>> items
        # [1, 2, 9, 7, 3, 10]
        # >>> heapq.heappop(items) #heap在pop时总是将最小值首先pop出
        # 1
        # >>> items
        # [2, 3, 9, 7, 10]


