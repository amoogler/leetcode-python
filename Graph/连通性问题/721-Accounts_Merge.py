class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])

        return self.root[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)

        if root_x == root_y:
            return

        if self.rank[root_x] > self.rank[root_y]:
            self.root[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.root[root_x] = root_y
        else:
            self.root[root_y] = root_x
            self.rank[root_x] += 1


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        res = []
        L = len(accounts)
        uf = UnionFind(L)

        # Build a hashmap, unique email as key, account index as the value.
        emailToIndex = dict()

        for idx, account in enumerate(accounts):
            for email in account[1:]:
                if email in emailToIndex:
                    uf.union(idx, emailToIndex[email])
                else:
                    emailToIndex[email] = idx

        # Build a hashmap, account index as the key and list of unique emails as the value.
        indexToEmails = defaultdict(list)

        for email, idx in emailToIndex.items():
            root = uf.find(idx)
            indexToEmails[root].append(email)

        for idx, emails in indexToEmails.items():
            res.append([accounts[idx][0]] + sorted(emails))

        return res
