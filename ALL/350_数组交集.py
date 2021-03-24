class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 从短的数组开始，降低遍历复杂度

        (nums1, nums2) = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)

        freq_dict = collections.defaultdict(int)
        for item in nums1:
            freq_dict[item] += 1

        intersect_items = []

        for item in nums2:
            if item in freq_dict.keys():
                if freq_dict[item] > 0:
                    intersect_items.append(item)
                    freq_dict[item] -= 1

        return intersect_items
