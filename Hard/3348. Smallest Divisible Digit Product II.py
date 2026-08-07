class Solution(object):
    def smallestNumber(self, num, t):
        exp = {1:(0,0,0,0), 2:(1,0,0,0), 3:(0,1,0,0), 4:(2,0,0,0),
               5:(0,0,1,0), 6:(1,1,0,0), 7:(0,0,0,1), 8:(3,0,0,0), 9:(0,2,0,0)}

        # reduce t to powers of 2,3,5,7 only (digits 1-9 have no other prime factors)
        e2=e3=e5=e7=0
        while t % 2 == 0: t//=2; e2+=1
        while t % 3 == 0: t//=3; e3+=1
        while t % 5 == 0: t//=5; e5+=1
        while t % 7 == 0: t//=7; e7+=1
        if t != 1:
            return "-1"
        req = (e2, e3, e5, e7)

        def minimal_slots(a, b):
            best = None
            for r in range(0, min(a, b) + 1):
                ra = max(0, a - r); rb = max(0, b - r)
                cnt = r + (ra + 2)//3 + (rb + 1)//2
                if best is None or cnt < best:
                    best = cnt
            return best

        def feasible(k, req4):
            a,b,c,d = [max(0,x) for x in req4]
            if c + d > k:
                return False
            return minimal_slots(a, b) <= k - c - d

        def construct(k, req4):
            ra,rb,rc,rd = [max(0,x) for x in req4]
            rem_k = k
            res = []
            for pos in range(k):
                rem_k -= 1
                for cand in range(1, 10):
                    ea,eb,ec,ed = exp[cand]
                    na = max(0, ra-ea); nb = max(0, rb-eb)
                    nc = max(0, rc-ec); nd = max(0, rd-ed)
                    if nc + nd <= rem_k and minimal_slots(na, nb) <= rem_k - nc - nd:
                        res.append(str(cand))
                        ra,rb,rc,rd = na,nb,nc,nd
                        break
            return "".join(res)

        s = num
        L = len(s)
        digs = [int(ch) for ch in s]

        pre = [(0,0,0,0)]
        for i in range(L):
            e = exp.get(digs[i], (0,0,0,0))
            p = pre[-1]
            pre.append((p[0]+e[0], p[1]+e[1], p[2]+e[2], p[3]+e[3]))

        zero_pos = s.find('0')

        # try num itself
        if zero_pos == -1:
            a,b,c,d = pre[L]
            if a>=req[0] and b>=req[1] and c>=req[2] and d>=req[3]:
                return s

        limit = zero_pos if zero_pos != -1 else L-1
        for i in range(limit, -1, -1):
            prefix_exp = pre[i]
            for d in range(digs[i]+1, 10):
                e = exp[d]
                combined = tuple(prefix_exp[j]+e[j] for j in range(4))
                rem = tuple(req[j]-combined[j] for j in range(4))
                k = L - i - 1
                if feasible(k, rem):
                    return s[:i] + str(d) + construct(k, rem)

        # no same-length answer, go one length up
        k0 = minimal_slots(req[0], req[1]) + req[2] + req[3]
        target_len = max(L+1, k0)
        return construct(target_len, req)
