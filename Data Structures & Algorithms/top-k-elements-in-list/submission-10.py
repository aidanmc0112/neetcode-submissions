class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        # Count how many times each number appears
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        # Sort by frequency (highest first)
        sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)

        answer = []
        for i in range(k):
            answer.append(sorted_count[i][0])

        return answer