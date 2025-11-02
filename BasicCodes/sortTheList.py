def two_sum_sorted(nums,target):
    left,right = 0, len(nums) - 1

    while left < right :
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left+1, right+1]
        elif current_sum < target:
            left +=1
        else:
            right -=1

print(two_sum_sorted([2,7,11,15], 9))       # [1,2]
print(two_sum_sorted([1,2,3,4,6], 6))       # [2,4]
print(two_sum_sorted([-3,-1,0,2,4,5], 1))   # [2,5]
            