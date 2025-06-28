from collections import defaultdict


class UnionFind:
    def __init__(self, size: int):
        # Initialize parent and rank for each node
        self.parent = {i: i for i in range(size)}
        self.rank = {i: 0 for i in range(size)}

    def find(self, x: int) -> int:
        # Path compression
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        # Union by rank
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False

        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        num_accounts = len(accounts)
        uf = UnionFind(num_accounts)

        # Maps each email to its corresponding account index
        email_to_account_index = {}

        # Union accounts that share common emails
        for account_index, account in enumerate(accounts):
            for email in account[1:]:
                if email not in email_to_account_index:
                    email_to_account_index[email] = account_index
                else:
                    uf.union(account_index, email_to_account_index[email])

        # Group emails by their root account index
        root_index_to_emails = defaultdict(list)
        for email, account_index in email_to_account_index.items():
            root_index = uf.find(account_index)
            root_index_to_emails[root_index].append(email)

        # Build the final result: name + sorted list of emails
        merged_accounts = []
        for root_index, emails in root_index_to_emails.items():
            name = accounts[root_index][0]
            merged_accounts.append([name] + sorted(emails))

        return merged_accounts
