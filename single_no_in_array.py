#Given an array of N integers. Every number in the array except one appears twice. Find the single number in the array.

class Solution:
    def singleNonDuplicate(self, arr):
        # Get the size of the array
        n = len(arr)

        # If array has only one element, return it
        if n == 1:
            return arr[0]

        # Loop through the array
        for i in range(n):
            # Check if it's the first element and not equal to the next
            if i == 0:
                if arr[i] != arr[i + 1]:
                    return arr[i]

            # Check if it's the last element and not equal to the previous
            elif i == n - 1:
                if arr[i] != arr[i - 1]:
                    return arr[i]

            # Check if the current element is not equal to both neighbors
            else:
                if arr[i] != arr[i - 1] and arr[i] != arr[i + 1]:
                    return arr[i]

        # Dummy return if no element found
        return -1

# Driver code
if __name__ == "__main__":
    # Input array with one unique element
    arr = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]

    # Create an object of Solution class
    obj = Solution()

    # Call the function and store result
    ans = obj.singleNonDuplicate(arr)

    # Print the result
    print("The single element is:", ans)
