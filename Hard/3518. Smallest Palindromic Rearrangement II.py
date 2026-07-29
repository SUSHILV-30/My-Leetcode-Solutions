from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = Counter(s)
        odd_chars = [c for c, cnt in freq.items() if cnt % 2 == 1]
        middle = odd_chars[0] if odd_chars else ''

        # Only the first half matters — halve every count
        half_counts = {c: cnt // 2 for c, cnt in freq.items() if cnt // 2 > 0}
        half_len = sum(half_counts.values())

        def comb_capped(n, r, cap):
            # C(n, r), but stop early once it exceeds cap (avoids huge numbers)
            if r < 0 or r > n:
                return 0
            r = min(r, n - r)
            result = 1
            for i in range(1, r + 1):
                result = result * (n - r + i) // i
                if result > cap:
                    return cap + 1
            return result

        def count_arrangements(counts, remaining_total, cap):
            result = 1
            rem = remaining_total
            for c in sorted(counts.keys()):
                cnt = counts[c]
                if cnt == 0:
                    continue
                result *= comb_capped(rem, cnt, cap)
                if result > cap:
                    return cap + 1
                rem -= cnt
            return result

        total = count_arrangements(half_counts, half_len, k)
        if total < k:
            return ""

        half = []
        counts = dict(half_counts)
        remaining_total = half_len
        letters = sorted(counts.keys())

        for _ in range(half_len):
            for c in letters:
                if counts.get(c, 0) == 0:
                    continue
                counts[c] -= 1
                remaining_total -= 1
                cnt = count_arrangements(counts, remaining_total, k)
                if cnt >= k:
                    half.append(c)
                    break
                else:
                    k -= cnt
                    counts[c] += 1
                    remaining_total += 1

        half_str = ''.join(half)
        return half_str + middle + half_str[::-1]
