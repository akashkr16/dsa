#Given two sorted arrays, arr1, and arr2 of size n and m. Find the union of two sorted arrays.
#The union of two arrays can be defined as the common and distinct elements in the two arrays.

class Solution:
    # Function to find the union of two arrays using set
    def findUnion(self, arr1, arr2):
        # Create a set with elements from both arrays
        st = set(arr1) | set(arr2)  # Union of two sets

        # Return sorted list
        return sorted(st)

# Driver code
arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [2, 3, 4, 4, 5, 11, 12]

obj = Solution()
result = obj.findUnion(arr1, arr2)

print("Union of arr1 and arr2 is:", *result)
