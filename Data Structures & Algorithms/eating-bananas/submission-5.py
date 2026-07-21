import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #piles.sort()
        #last = len(piles)-1
        #upper_bound = piles[last]
        #lower_bound = 1
        #hours = 0;
        #while lower_bound <= upper_bound:
            #do something like piles[i] / lower bound = hours for that pile
            #hours = 0
            #for i in range(0, len(piles)):
                #a = piles[i]
                #hours += math.ceil(a / lower_bound) 
            #if hours <= h:
                #return lower_bound
            #else: 
                #lower_bound+=1
        left = 1
        right = max(piles)
        while left <= right:
            mid = (left + right) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)
            if hours <= h:
                right = mid - 1
            else:
                left = mid + 1
        return left