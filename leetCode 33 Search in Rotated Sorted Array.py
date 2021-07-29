# https://leetcode.com/problems/search-in-rotated-sorted-array/
# http://pythontutor.com/visualize.html#code=def%20search%28nums,%20target%29%3A%0A%20%20%20%20left,%20right%20%3D%200,%20len%28nums%29%20-%201%0A%20%20%20%20if%20len%28nums%29%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20return%20-1%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20while%20left%20%3C%3D%20right%3A%0A%20%20%20%20%20%20%20%20mid%20%3D%20%28left%20%2B%20right%29%20//%202%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20if%20nums%5Bmid%5D%20%3D%3D%20target%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20mid%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20if%20nums%5Bmid%5D%20%3E%3D%20nums%5Bleft%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20nums%5Bleft%5D%20%3C%3D%20target%20%3C%20nums%5Bmid%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20right%20%3D%20mid%20-%201%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20left%20%3D%20mid%20%20%2B%201%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20nums%5Bmid%5D%20%3C%20target%20%3C%3D%20nums%5Bright%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20left%20%3D%20mid%20%2B%201%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20right%20%3D%20mid%20-%201%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20return%20-1%0A%0Anums%20%3D%20%5B4,5,6,7,0,1,2%5D%0A%0Atarget%20%3D%200%0A%0Asearch%28nums,%20target%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
# https://bit.ly/3esQUaX

def search(nums, target):
    left, right = 0, len(nums) - 1
    if len(nums) == 0:
        return -1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] >= nums[left]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


nums = [4, 5, 6, 7, 0, 1, 2]

target = 0

print(search(nums, target))
