class Solution(object):
    def myAtoi(self, s):
        INT_MAX =  2**31 - 1
        INT_MIN = -2**31
        
        result = 0
        sign = 1
        started = False   # have we started reading digits?
        signed = False    # have we already seen a sign character?

        for i, x in enumerate(s):
            
            # Step 1: skip leading whitespace
            if x == ' ':
                if started or signed:  # space after digits/sign → stop
                    break
                continue
            
            # Step 2: handle sign (only before any digit)
            if x == '-' or x == '+':
                if started or signed:  # sign after digits → stop
                    break
                sign = -1 if x == '-' else 1
                signed = True
                continue

            # Step 3: read digits
            if x.isdigit():
                started = True
                result = result * 10 + int(x)  # int(x) gives digit value directly
            
            else:
                break  # non-digit, non-sign, non-space → stop

        # Step 4: apply sign and clamp
        result = result * sign
        result = max(INT_MIN, min(INT_MAX, result))

        return result
