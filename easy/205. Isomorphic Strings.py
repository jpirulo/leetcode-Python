def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    s_map = {}
    t_map = {}
    for i in range(len(s)):
        if s[i] not in s_map:
            s_map[s[i]] = t[i]
        if t[i] not in t_map:
            t_map[t[i]] = s[i]
        if s_map[s[i]] != t[i] or t_map[t[i]] != s[i]:
            return False
    return True



        
        


if __name__ == "__main__":
    print(isIsomorphic(s='badc', t='baba'))
