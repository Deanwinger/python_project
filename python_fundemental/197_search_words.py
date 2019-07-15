# leetcode 79. 单词搜索
# 剑指offer(2) 题 12
# 回溯法的经典应用

# 2019-7-15
class Solution:    
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        if not board:
            return False
        
        rows = len(board)
        cols = len(board[0])
        
        marked = [[False]*cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if self.in_path(board, word, 0, rows, cols, marked, r, c):
                    return True
        return False
    
    def in_path(self, board, word, word_length, rows, cols, marked, row, col):
        if len(word) <= word_length:
            return True
        
        has_path = False
        if 0<=row<rows and 0<=col<cols and not marked[row][col] and board[row][col] == word[word_length]:
            marked[row][col] = True
            has_path =  self.in_path(board, word, word_length+1, rows, cols, marked, row+1, col) or \
            self.in_path(board, word, word_length+1, rows, cols, marked, row-1, col) or \
            self.in_path(board, word, word_length+1, rows, cols, marked, row, col+1) or \
            self.in_path(board, word, word_length+1, rows, cols, marked, row, col-1)
            
            if not has_path:
                marked[row][col] = False
        return has_path


if __name__=='__main__':
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    s = Solution()
    print(s.exist(board, word))