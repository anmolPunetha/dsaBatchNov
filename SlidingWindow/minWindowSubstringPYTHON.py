class Solution:
    def check(self, s_map, t_map):
        # Everything in t should be in s
        # If s has anything extra, it's not a problem
        for i in range(128):
            if t_map[i] > s_map[i]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        # Save t in a map/array/list
        t_map = [0] * 128
        s_map = [0] * 128

        # Iterate over t and save in t_map
        for ch in t:
            t_map[ord(ch)] += 1

        # Start window translation
        start = 0
        ans_start = -1  # Final answer index
        ans_length = float('inf')  # Initialize to a very large number
        for i in range(len(s)):
            ch = s[i]
            # Expand
            s_map[ord(ch)] += 1

            # Shrink
            # If current availability (s_map) of the start character is extra than the requirement (t_map), we can shrink
            while start<=i and s_map[ord(s[start])] > t_map[ord(s[start])]:
                s_map[ord(s[start])] -= 1
                start += 1

            # Update
            if self.check(s_map, t_map):
                curr_size = i - start + 1
                if curr_size < ans_length:
                    ans_length = curr_size
                    ans_start = start

        # Generate the substring using ans_start and ans_length
        if ans_start == -1:
            return ""
        return s[ans_start: ans_start + ans_length]
