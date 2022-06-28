class Solution:
    def minDeletions(self, s: str) -> int:

        # Store the frequency of each character
        frequency = [0] * 26
        for char in s:
            frequency[ord(char) - ord("a")] += 1
        frequency.sort(reverse=True)

        delete_count = 0
        max_freq_allowed = len(s)

        for freq in frequency:
            if freq > max_freq_allowed:
                delete_count += freq - max_freq_allowed
                freq = max_freq_allowed

            max_freq_allowed = max(0, freq - 1)

        return delete_count
