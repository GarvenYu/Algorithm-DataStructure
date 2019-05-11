#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def generate_board(self, n):
        return [['.'] * n for _ in range(n)]

    def solveNQueens(self, n: int):
        ans = []
        if not n:
            return ans
        board = self.generate_board(n)
        for i in range(n):
            board[0][i] = 'Q'  # 第一行
            self.core(n, ans, board, 1)
            board[0][i] = '.'
        return ans

    def core(self, n, ans, board, current_row):
        if current_row == n:
            ans.append([''.join(l) for l in board])
        else:
            for i in range(n):
                if self.check(n, board, current_row, i):
                    board[current_row][i] = 'Q'
                    self.core(n, ans, board, current_row + 1)
                    board[current_row][i] = '.'

    def check(self, n, board, row, col):
        # 判断在同一列或对角线是否冲突
        for i in range(1, row + 1):
            if board[row - i][col] == 'Q':
                # 同一列
                return False
            # 对角线
            # 注意防止越界
            if col + i < n and board[row - i][col + i] == 'Q':
                return False
            if col - i >= 0 and board[row - i][col - i] == 'Q':
                return False
        return True


s = Solution()
s.solveNQueens(4)
