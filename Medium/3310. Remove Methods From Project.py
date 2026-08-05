class Solution:
    def remainingMethods(self, n, k, invocations):
        from collections import defaultdict, deque
        
        graph = defaultdict(list)
        for a, b in invocations:
            graph[a].append(b)
        
        
        suspicious = set()
        queue = deque([k])
        suspicious.add(k)
        while queue:
            node = queue.popleft()
            for nxt in graph[node]:
                if nxt not in suspicious:
                    suspicious.add(nxt)
                    queue.append(nxt)
        
        
        for a, b in invocations:
            if b in suspicious and a not in suspicious:
                return list(range(n))
        
        return [i for i in range(n) if i not in suspicious]
