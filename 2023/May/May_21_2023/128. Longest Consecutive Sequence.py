class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        parent = {}  # Parent dictionary to store the parent/root of each element
        rank = {}  # Rank dictionary to store the rank/size of each set

        # Initialize the parent and rank dictionaries
        for num in num_set:
            parent[num] = num
            rank[num] = 1

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x != root_y:
                if rank[root_x] > rank[root_y]:
                    parent[root_y] = root_x
                    rank[root_x] += rank[root_y]
                else:
                    parent[root_x] = root_y
                    rank[root_y] += rank[root_x]

        max_length = 1

        for num in num_set:
            if num - 1 in num_set:  # Check if there is a smaller consecutive number
                union(num, num - 1)

        for num in num_set:
            root = find(num)
            max_length = max(max_length, rank[root])

        return max_length
