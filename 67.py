class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_ptr, b_ptr = len(a) - 1, len(b) - 1
        carry = 0
        queue = collections.deque()

        while a_ptr >= 0 or b_ptr >= 0:
            while a_ptr >= 0 and b_ptr >= 0:
                a_bit, b_bit = int(a[a_ptr]), int(b[b_ptr])
                curr_bit = a_bit ^ b_bit ^ carry
                queue.appendleft(str(curr_bit))
                carry = 1 if (a_bit + b_bit + carry) > 1 else 0
                a_ptr -= 1
                b_ptr -= 1

            while a_ptr >= 0:
                a_bit = int(a[a_ptr])
                curr_bit = a_bit ^ carry
                queue.appendleft(str(curr_bit))
                carry = 1 if (a_bit + carry) > 1 else 0
                a_ptr -= 1

            while b_ptr >= 0:
                b_bit = int(b[b_ptr])
                curr_bit = b_bit ^ carry
                queue.appendleft(str(curr_bit))
                carry = 1 if (b_bit + carry) > 1 else 0
                b_ptr -= 1

            if carry > 0:
                queue.appendleft(str(carry))

        return ''.join(queue)
