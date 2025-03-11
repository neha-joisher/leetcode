class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()  # Step 1: Remove leading whitespace
        if not s:
            return 0

        sign = 1
        i = 0
        if s[i] == '-' or s[i] == '+':  # Step 2: Check for sign
            sign = -1 if s[i] == '-' else 1
            i += 1

        num = 0
        while i < len(s) and s[i].isdigit():  # Step 3: Process digits
            num = num * 10 + int(s[i])
            i += 1

        num *= sign  # Apply the sign

        # Step 4: Clamp the result within the 32-bit range
        int_min, int_max = -2**31, 2**31 - 1
        if num < int_min:
            return int_min
        if num > int_max:
            return int_max
        return num