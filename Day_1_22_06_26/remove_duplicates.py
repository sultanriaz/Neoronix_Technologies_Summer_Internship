def remove_duplicates(nums):
    if not nums:
        return 0
    i=0
    for j in range (1, len(nums)-1):
        if nums[j]!=nums[i]:
            i+=1
            nums[i]=nums[j]
    return i+1
list=([1,2,3,4,4,5,7])       
remove_duplicates(list)
print(list)