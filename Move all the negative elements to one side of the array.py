Question - Move all the negative elements to one side of the array 

[ Link - https://www.geeksforgeeks.org/problems/move-all-negative-elements-to-end1813/1 ]

Solution :

class Solution:
    def segregateElements(self, arr):
        
        # Normal Method of Differnt Array Creation for Positive and Negative Values and Applying Inplace Slicing
        # TC : O(n) , SC : O(n)
      
        l = [] ; h = []
        for i in arr:
            if i>=0:
                l.append(i)
            else:
                h.append(i)
        arr[:] = l+h
        return arr
        
        
