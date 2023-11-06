class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # check if board has sufficient characters for word
        # flatten board to list of chars
        x = sum(board, [])
        if Counter(word) - Counter(x):
            return False

        # find the first char, then word search
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.check(i,j,0, word, board):
                    return True

        return False

    def check(self, i,j, index, word, board):
        if index == len(word):
            return True

        if i<0 or j<0 or i>=len(board) or j>=len(board[0]):
            return False

        if board[i][j]== word[index]:
            # prevent use of same letter
            temp= board[i][j]
            board[i][j]= -1
            if (
                self.check(i-1,j, index+1, word, board) or
                self.check(i+1,j, index+1, word, board) or
                self.check(i,j-1, index+1, word, board) or
                self.check(i,j+1, index+1, word, board)
            ):
                return True

            board[i][j]= temp

        return False
