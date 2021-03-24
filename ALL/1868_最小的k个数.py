# https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []

        hp = [-x for x in arr[:k]]

        # 用数组中前 k 个去建立一个堆

        heapq.heapify(hp)

        # 然后遍历数组中后面的元素
        # 如果比堆 root 小，那么 pop root，插入这个新元素
        for i in range(k, len(arr)):
            if -hp[0] > arr[i]:
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])

        ans = [-x for x in hp]

        return ans

