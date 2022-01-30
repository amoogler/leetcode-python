class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        pos = 0
        res = []

        while pos < len(words):
            k = self.get_next_k_words(pos, words, maxWidth)
            line = self.pad_with_space(pos, k, words, maxWidth)
            res.append(line)
            pos += k

        return res


    def get_next_k_words(self, pos, words, maxWidth):
        curr_len = len(words[pos])
        k = 1

        while pos + k < len(words) and len(words[pos + k]) + 1 + curr_len <= maxWidth:
            curr_len += (1 + len(words[pos + k]))
            k += 1

        return k


    def pad_with_space(self, pos, k, words, maxWidth):
        standard_spacing = ' '.join(words[pos:pos + k])
        L = len(standard_spacing)
        res = ''

        # Line only has one word OR the last line, pad spaces at the end.
        if k == 1 or pos + k == len(words):
            total_spaces = maxWidth - L
            res = standard_spacing + ' ' * total_spaces
        else:
            total_gaps = k - 1
            total_spaces = maxWidth - L + total_gaps
            avg_spaces = total_spaces // total_gaps
            leftover_spaces = total_spaces % (k - 1)

            if leftover_spaces > 0:
                res += (' ' * (avg_spaces + 1)).join(words[pos:pos + leftover_spaces])
                res += (' ' * (avg_spaces + 1))

            res += (' ' * avg_spaces).join(words[pos + leftover_spaces:pos + k])

        return res
