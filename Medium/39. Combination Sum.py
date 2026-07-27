class Solution(object):
    def combinationSum(self, candidates, target):
        candidates.sort()
        result = []
        path = []
        self.backtrack(candidates, target, 0, path, result)
        return result

    def backtrack(self, candidates, remaining, start, path, result):
        if remaining == 0:
            result.append(path[:])   # save a copy of the current combination
            return

        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break  # sorted — no point trying larger ones

            path.append(candidates[i])
            self.backtrack(candidates, remaining - candidates[i], i, path, result)  # i, not i+1 → allows reuse
            path.pop()  # undo the choice, try the next candidate
