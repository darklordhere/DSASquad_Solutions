Question - Find the "Kth" max and min element of an array 
[ Link - https://practice.geeksforgeeks.org/problems/kth-smallest-element/0 ]

Solution :

def kthSmallest(self, arr,k):
        
        # By Sorting 
        # TC : O(nlogn) , SC : O(1)
        
        arr.sort()
        return arr[k-1]
        
        
        # Swapping till k with left side sort
        # TC : O(k*n) ~ (n^2 if k close to n) , SC : O(1)
        for i in range(k):
            for j in range(i+1,len(arr)):
                if arr[i]>arr[j]:
                    arr[i],arr[j] = arr[j],arr[i]
        return arr[k-1]
        
        
        # Heap Implementation (k+(smallest/largest))
        # Soln - If smallest - MaxHeap & If largest - MinHeap
        # TC : O(nlogk) , SC : O(k)
        
        import heapq
        x = []
        for i in arr:
            heapq.heappush(x,-i)
            if len(x)>k:
                heapq.heappop(x)
            heapq.heapify(x)
        # print(x)
        return -heapq.heappop(x)
        
