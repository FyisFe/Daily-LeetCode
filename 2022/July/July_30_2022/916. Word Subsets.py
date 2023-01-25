class Solution:
    def wordSubsets(self, words1, words2):
        def getWordLetterHashMap(word):
            hm = {}
            for letter in word:
                if letter in hm:
                    hm[letter] += 1
                else:
                    hm[letter] = 1
            return hm

        requiredLetterHashMap = {}

        for word in words2:
            hm = getWordLetterHashMap(word)
            for key in hm:
                if (
                    key not in requiredLetterHashMap
                    or requiredLetterHashMap[key] < hm[key]
                ):
                    requiredLetterHashMap[key] = hm[key]

        ans = []
        for word in words1:
            hm = getWordLetterHashMap(word)
            isUniversal = True
            for key in requiredLetterHashMap:
                if key not in hm or hm[key] < requiredLetterHashMap[key]:
                    isUniversal = False
            if isUniversal:
                ans.append(word)

        return ans
