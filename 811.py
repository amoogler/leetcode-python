class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_count = collections.defaultdict(int)
        res = []

        for cpdomain in cpdomains:
            parts = cpdomain.split()
            count, domain = int(parts[0]), parts[1]

            for i in range(len(domain) - 1, -1, -1):
                if domain[i] == '.':
                    domain_count[domain[i + 1 :]] += count
                elif i == 0:
                    domain_count[domain] += count

        for k, v in domain_count.items():
            res.append(' '.join([str(v), k]))

        return res
