# Given an array of length N, peak element is defined as the element greater than both of its neighbors. Formally, if arr[i] is the peak element, arr[i - 1] < arr[i] and arr[i + 1] < arr[i]. Find the index(0-based) of a peak element in the array. If there are multiple peak numbers, return the index of any peak number.

# Function to find a peak element in the array
    def findPeakElement(self, nums):
        n = len(nums)

        # Traverse the array
        for i in range(n):
            # Check left neighbor if exists
            left = (i == 0) or (nums[i] >= nums[i - 1])
            # Check right neighbor if exists
            right = (i == n - 1) or (nums[i] >= nums[i + 1])

            # If both conditions are true
            if left and right:
                return i

        # In case no peak found
        return -1

# Driver
sol = Solution()
nums = [1, 3, 20, 4, 1, 0]
index = sol.findPeakElement(nums)
print(f"Peak at index: {index} with value: {nums[index]}")
