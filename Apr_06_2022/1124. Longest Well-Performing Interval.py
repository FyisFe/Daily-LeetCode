class Solution:
    def longestWPI(self, hours):
        max_wpi, ntv, first_preimage = 0, 0, {}

        for day_idx, hrs_today in enumerate(hours):
            ntv += 1 if hrs_today > 8 else -1

            if ntv > 0:
                max_wpi = day_idx + 1

            if not ntv in first_preimage:
                first_preimage[ntv] = day_idx

            if ntv - 1 in first_preimage:
                max_wpi = max(max_wpi, day_idx - first_preimage[ntv - 1])

        return max_wpi
