class Solution(object):
    def simplifyPath(self, path):
        n = len(path)
        result = []      # will hold the final directory names, in order
        current = ""      # builds up each token between slashes

        for i in range(n):
            if path[i] != "/":
                current += path[i]

            # process 'current' when we hit a slash, or reach the end of the string
            if path[i] == "/" or i == n - 1:
                if current == "" or current == ".":
                    pass  # nothing to do, skip
                elif current == "..":
                    if result:
                        result.pop()
                else:
                    result.append(current)
                current = ""  # reset for the next token

        return "/" + "/".join(result)
