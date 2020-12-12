class Solution:
    def letterCasePermutation(self, S: str):
        ret = []
        li = []

        def make_list():
            for char in S:
                li.append(char)

        def backtrack(i):
            if i == len(li):
                ret.append("".join(li))
                return
            if '0' <= li[i] <= '9':
                backtrack(i + 1)
            else:
                li[i] = li[i].lower()
                backtrack(i + 1)
                li[i] = li[i].upper()
                backtrack(i + 1)

        make_list()
        backtrack(0)
        return ret
