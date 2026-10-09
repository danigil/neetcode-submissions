from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        d_r = defaultdict(set)
        d_c = defaultdict(set)
        d_b = defaultdict(set)

        for r in range(9): 
            for c in range(9):
                curr_val=board[r][c]
                if curr_val == ".":
                    continue

                if curr_val in d_r[r] \
                or curr_val in d_c[c] \
                or curr_val in d_b[(int(r)//3, int(c)//3)]:
                    return False

                d_r[r].add(curr_val)
                d_c[c].add(curr_val)
                d_b[(int(r)//3, int(c)//3)].add(curr_val)
        return True

        