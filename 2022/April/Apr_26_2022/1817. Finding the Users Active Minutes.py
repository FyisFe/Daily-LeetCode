class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:

        dictionary = {}

        answer = [0] * k

        for user in logs:
            if user[0] in dictionary:
                dictionary[user[0]].add(user[1])
            else:
                dictionary[user[0]] = set({user[1]})

        for value in dictionary.values():
            if len(value) <= k:
                answer[len(value) - 1] += 1

        return answer
