class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(start: int, end: int) -> None:
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1

        N = len(s)
        reverse(0, N - 1)
        start, end = 0, 0

        while end < N:
            if s[end] == ' ':
                reverse(start, end - 1)
                start = end + 1
            elif end == N - 1:
                reverse(start, end)

            end += 1

        return s