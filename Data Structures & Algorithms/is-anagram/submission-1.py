class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}

        for i in s:
            if i in s_map:
                s_map[i] += 1
            else:
                s_map[i] = 1
        for i in t:
            if i in t_map:
                t_map[i] += 1
            else:
                t_map[i] = 1
        if s_map == t_map:
            return True
        else:
            return False
    # Build two hash maps → O(N + M) time
    # compare them -> O(K) where K in the len of unique characters
    # space compexity - 2 * O(K) for the two maps
