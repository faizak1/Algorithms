# This Python program demonstrates how recursive algorithms for bubble sort and insertion sort run slower than the iterative versions
# and also demonstrates that selection sort is faster than bubble sort

import random
import time

# RandList: function to generate random numbers in the given [start, end] range and save them in a list. The list is returned 
def RandList (start, end, len):
        res = [] # an empty list

        for j in range (len):
                res.append (random.randint(start,end))
                
        return res

def swap (x,y):
        tmp=x
        x=y
        y=tmp


# FindMinimum: return the index of smallest element in l[left...right]
def FindMinimum (l, left, right):

        # minV is the minimum value so far
        # in the beginning, first value is the smallest ... 
        minV = l[left]
        minI = left

        for i in range (left,right+1): # i=left, left+1, ... right
                if l[i]<minV:
                        minV = l[i]
                        minI = i

                # loop invariant
                # minV = min (l[left...i]), i.e., min. value seen so far 
                # minV = l[minI]

        return minI

#recursiveSelectionSort
def SelectionSort (l):
        listlen=len(l)

        for i in range(listlen): # i=0, 1, 2, ..., listlen-1
                #find index of smallest element in l[i...listlen-1]
                minIndex = FindMinimum (l, i, listlen-1)

                
                if minIndex!=i:
                        l[i],l[minIndex]=l[minIndex],l[i]

def BubbleSort(l):
        listlen=len(l)

        for j in range(listlen): # j=0,1, ... listlen-1

                # compare adjacent elements, swap them if they are in the wrong order 
                for i in range(listlen-1): # i=0, 1, listlen-2
                        if l[i]>l[i+1]:
                                l[i],l[i+1]=l[i+1],l[i]
                                
def IsSorted (l):
        listlen = len(l)
        for i in range(listlen-1): ## i=0,1, ... listlen-2
                if l[i]>l[i+1]:
                        print(l[i],l[i+1])
                        return False

        return True
    
#selection sort the given part of a vector of int into ascending order
# @param l: the list to be sorted, list.length() gives the size of the list
# @param left, right: specify the range of list to be sorted
# @pre: l has been initialized with a certain number of elements, left<=right
# @post: elements in l[left…right] has been rearranged into ascending order 
def RecursiveSelectionSort(l1, left, right):
    if (left==right):
        return;

    S=FindMinimum(l1, left, right)

    if (S!=left):
        l1[left], l1[S] = l1[S], l1[left]
        #swap(l1[left], l1[S])

    RecursiveSelectionSort(l1, left+1, right)
   
# FindMaximum: returns the index of largest element in l[left...right]
def FindMaximum (l, left, right):

        # maxNum is the max value so far
        # in the beginning, first value is the largest ... 
        maxNum = l[left]
        maxI = left

        for i in range (left,right+1): ## i=left, left+1, ... right
                if l[i]>maxNum:
                        maxNum = l[i]
                        maxI = i

                # loop invariant
                # minV = min (l[left...i]), i.e., min. value seen so far 
                # minV = l[minI]

        return maxI    

#recursiveBubbleSort
def RecursiveBubbleSort(l2, left, right): 
    if (left==right):
        return
 
    S=FindMaximum(l2, left, right)

    if (S!=right):
        l2[right], l2[S] = l2[S], l2[right]

    RecursiveBubbleSort(l2, left, right-1)

# testing bubble sort, by visual checking output 
a=[20,3,4,6,1]
BubbleSort(a)
if IsSorted(a)==False:
        print('bubblesort not working')
print(a)

# Testing selection sort using IsSorted() to verify if list is sorted or not 
cl=['a','z','d','g','m']
print(cl)
SelectionSort(cl)
if IsSorted(cl)==False:
        print('not working')
print(cl)

# testing recurisve selection sort
l1 = [5, 4, 82, 101, 99]
print("l1 (input for testing recursive selection sort) is" , l1)
left = 0
right = len(l1)-1
RecursiveSelectionSort(l1, left, right)
if IsSorted(l1)==False:
        print('not working')
print(l1)

l2 = [16, 6, 82, 101, 71,4]
print("l2 (input for testing recursive bubble sort) is" , l2)
left = 0
right = len(l2)-1
RecursiveBubbleSort(l2, left, right)
if IsSorted(l2)==False:
        print('not working')
print(l2)

print ("Length ",  "      BubbleSort ",  "       RecursiveBubbleSort ",  
       "        SelectionSort ",  
       "         RecursiveSelectionSort ")
print ()

for i in range(10,2000,20): ## i=10,30,50,70, ... 1990OB
        l=RandList(1,1000,i)
        #print (l)
        start_time = time.time()
        BubbleSort(l)
        end_time = time.time()
        firstTime = end_time-start_time
        
        list2=RandList(1,1000,i)
        left = 0
        right = len(list2)-1
        start_time2 = time.time()
        RecursiveBubbleSort(list2, left, right)
        end_time2 = time.time()
        secondTime = end_time2 - start_time2
        
        list3=RandList(1,1000,i)
        start_time3 = time.time()
        SelectionSort(list3)
        end_time3 = time.time()
        thirdTime = end_time3 - start_time3
        
        list4=RandList(1,1000,i)
        left = 0
        right = len(list4)-1
        start_time4 = time.time()
        RecursiveSelectionSort(list4, left, right)
        end_time4 = time.time()
        fourthTime = end_time4 - start_time4
         
        print (i, 'elapsed:',   firstTime, '  ', secondTime,  '  ', thirdTime, '  ', fourthTime)	
