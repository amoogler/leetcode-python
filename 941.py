class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        length, i = len(arr), 0

        # Up hill.
        while i < length - 1 and arr[i] < arr[i + 1]:
            i += 1

        # Peak position cannot be at first or last index.
        if i == 0 or i == length - 1:
            return False

        # Down hill.
        while i < length - 1 and arr[i] > arr[i + 1]:
            i += 1

        return i == length - 1
