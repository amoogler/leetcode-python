class Solution:
    def addOperators(self, s: str, target: int) -> List[str]:
        def backtrack(i, path, curr_result, prev_num):
            if i == len(s):
                if curr_result == target:
                    ans.append(path)

                return

            for j in range(i, len(s)):
                # Skip leading 0 cases.
                if j > i and s[i] == '0':
                    break

                num = int(s[i:j + 1])

                if i == 0:
                    # First num, pick it without adding any operator.
                    backtrack(j + 1, path + str(num), curr_result + num, num)
                else:
                    backtrack(j + 1, path + '+' + str(num), curr_result + num, num)
                    backtrack(j + 1, path + '-' + str(num), curr_result - num, -num)
                    backtrack(j + 1, path + '*' + str(num), curr_result - prev_num + prev_num * num, prev_num * num) # 1 + 2 * 3 * 4

        ans = []
        backtrack(0, "", 0, 0)
        return ans
