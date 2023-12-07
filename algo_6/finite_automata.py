class KMP:

    def __init__(self, pat=""):
        self.pat = pat
        alph = set(pat)
        m = len(pat)

        self.dfa = {char: [0]*m for char in alph}

        self.dfa[pat[0]][0] = 1
        X = 0
        
        for j in range(1, m):
            for char in alph:
                self.dfa[char][j] = self.dfa[char][X]
            self.dfa[pat[j]][j] = j+1
            X = self.dfa[pat[j]][X]

    def search(self, txt):
        indexes = []
        i, j, N, M = 0, 0, len(txt), len(self.pat)
        while i < N:
            if (j == M):
                indexes.append(i - M) 
                j = 0
            j = self.dfa[txt[i]][j]
            i += 1

        return indexes


if __name__ == '__main__':
    txt = "ababaagabagaba"
    pattern1 = "agab"
    pattern2 = "baag"

    kmp1 = KMP(pattern1)
    kmp2 = KMP(pattern2)
    
    result1 = kmp1.search(txt)
    print(result1)

    result2 = kmp2.search(txt)
    print(result2)

    print("?")
