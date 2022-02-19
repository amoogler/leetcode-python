class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank_set = set(bank)
        options = {
            'A' : ['C', 'G', 'T'],
            'C' : ['A', 'G', 'T'],
            'G' : ['A', 'C', 'T'],
            'T' : ['A', 'C', 'G']
        }

        queue = deque([start])
        seen = {start}
        res = 0

        while queue:

            queue_length = len(queue)

            for _ in range(queue_length):
                gene = queue.popleft()

                if gene == end:
                    return res

                for i in range(8):
                    temp = gene

                    for nc in options[gene[i]]:
                        gene = list(gene)
                        gene[i] = nc
                        gene = ''.join(gene)

                        if gene not in bank_set:
                            continue

                        if gene in seen:
                            continue

                        queue.append(gene)
                        seen.add(gene)

                    gene = temp

            res += 1

        return -1
