# f(['a','b','c'])
# return:
# abc
# acb
# bca
# bac
# cab
# cba

# board = ['a','b','c']

# for f in board:
#     # print(board.index(f), f)
#     for h in board:
#         print(board.index(h), h)



    
    # board[x] + board[x+1] + board[x+2]

# for f in range(len(board)):

#     board[f+1] + board[f+2]
#     board[f+2] + board[f+1]

import itertools
print(list(itertools.permutations(['a', 'b', 'c'])))