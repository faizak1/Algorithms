## Demonstration of Merge Sort Algorithm

## IsSorted: returns true if a list is sorted in ascending order, returns false otherwise
def IsSorted (l):
    listlen = len(l)
    for i in range(listlen-1): ## i=0,1, ... listlen-2
        if l[i]>l[i+1]:
            print(l[i],l[i+1])
            return False
        return True

## MergeSort: sorts l[left...right] in ascending order
def MergeSort (l, left, right):
    print ("MergeSort called (",l, left,right,")")
    if left>=right:
        print ("Returning from MergeSort (",l,left,right,")")
        return;
    else:
        mid = (left+right)//2
        MergeSort (l, left, mid)
        MergeSort (l, mid+1, right)
        #merge sorted sublists l[left...mid], l[mid+1] into a sorted whole
        s=[] ## create a staging area
        i = left
        j = mid+1
        while i<=mid and j<=right:
            if l[i]<=l[j]:
                s.append (l[i])
                i=i+1
            else:
                s.append (l[j])
                j = j+1
        ## copy left-over of either sublist into s
        while i<=mid:
            s.append (l[i])
            i=i+1
while j<=right:
    s.append(l[j])
    j=j+1
        ## copy elements from s to l
        for i in range(len(s)):  ##i=0,1...,len(s)-1
            l[i+left] = s[i]
        print ("Returning from MergeSort (",l,left,right,")")

a=[20,3,4,6,1]
MergeSort (a,0,len(a)-1)
if IsSorted(a)==False:
    print('MergeSort not working')
print(a)
