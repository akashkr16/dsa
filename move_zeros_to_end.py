#You are given an array of integers, your task is to move all the zeros in the array to the end of the array and move non-negative integers to the front by maintaining their order.

class Solution:
    # Function to move all zeroes to end
    def moveZeroes(self, arr):
        # Create temp array
        temp = [0] * len(arr)

        # Pointer to fill temp
        index = 0

        # Traverse input array
        for num in arr:
            # If non-zero, copy to temp
            if num != 0:
                temp[index] = num
                index += 1

        # Copy temp back to original
        for i in range(len(arr)):
            arr[i] = temp[i]

        # Return updated array
        return arr

# Main function
def main():
    arr = [0, 1, 0, 3, 12]
    sol = Solution()
    result = sol.moveZeroes(arr)
    
    # Print result
    print("Array after moving zeroes:", end=" ")
    for num in result:
        print(num, end=" ")
    print()

# Driver code
main()
