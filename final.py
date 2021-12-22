def main(nums):
    nums.sort()
    length = len(nums)-1
    htgnel = 0
    pendejo = 0
    
    pendejo = 0
    i = 0
    j = len(nums)-1

    while htgnel < length:
        pendejo = max(pendejo, nums[htgnel]+nums[length])
        htgnel += 1
        length -= 1

    return pendejo

