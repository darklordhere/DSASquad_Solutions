Question - Find the maximum and minimum element in an array
Link - [ https://www.geeksforgeeks.org/maximum-and-minimum-in-an-array/ ]

class Solution:
    def get_min_max(self, arr):
        
        # Brute Force - Min & Max Variable Store with Single Loop
        # TC : O(n) , SC : O(1)
        
        import math
        minn = math.inf
        maxx = -math.inf
        for i in arr:
            if i > maxx:
                maxx = i
            if i < minn:
                minn = i
        return [minn,maxx]
        
        
        # With Buit-in Function
        # TC : O(n) , SC : O(1)
        return [min(arr),max(arr)]
        
        # With Sorting
        # TC : O(n) , SC : O(1)
        arr.sort()
        return [arr[0],arr[-1]]
