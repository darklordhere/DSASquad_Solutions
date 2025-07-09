Question - Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo

[ Link - https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s/0 ]

Solution :

class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        
        # By HashMap for Count Store 
        # TC : O(n) , SC : O(1)
        
        d = dict()
        for i in arr:
            if d.get(i,-1)==-1:
                d[i]=1
            else:
                d[i]+=1
                
        zero=0 ; one=0 ; two=0
        
        for i,j in d.items():
            if i==0:
                zero=j
            if i==1:
                one=j
            if i==2:
                two=j
        arr[:] = ([0]*zero) + ([1]*one) + ([2]*two)
        return arr
        

        
        # Dutch National Flag Algorithm
        # TC : O(n) , SC : O(1)
        
        l=0 ; h=len(arr)-1 ; m = 0
        
        while m<=h:
            
            # Stores 0 in Start - Swap 0 if encountered and increase m
            if arr[m]==0:
                arr[l],arr[m]=arr[m],arr[l]
                l+=1
                m+=1
            
            # Stores 1 in the Mid - Do Nothing as it is already 1
            elif arr[m]==1:
                m += 1
                
            # Stores 2 in the End - Just Swap 2 with the mid value and decrease h
            else:
                arr[h],arr[m]=arr[m],arr[h]
                h-=1
                
        return arr
                
                
                
                
                
                
                
                
                
                
                
