Question - Reverse the array 
[Link - https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/]


class Solution:
    def reverseArray(self, arr):
        # By Recursion Solution
        # TC : O(n) , SC : O(n)
        
        def recursion_reverse(arr,i,j):
            if i>j:
                return
            arr[i],arr[j] = arr[j],arr[i]
            return recursion_reverse(arr,i+1,j-1)
        return recursion_reverse(arr,0,len(arr)-1)
        
        
        # InPlace Slicing Reverse Solution
        # TC : O(n) , SC : O(1)
        arr[:]=arr[::-1]
        return arr
        
        
        # Two Pointers Solution
        # TC : O(n) , SC : O(1)
        i,j = 0,len(arr)-1
        while i<j:
            arr[i],arr[j]=arr[j],arr[i]
            i += 1
            j -= 1
        return arr
        
