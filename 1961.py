class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        curr = ""
        N = len(s)

        for word in words:
            curr += word

            if len(curr) > N:
                break

            if s == curr:
                return True

        return False
