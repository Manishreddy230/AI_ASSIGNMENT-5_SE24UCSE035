import math
import random

class TicTacToe:

    def __init__(self, board=None):
        if board:
            self.board = board[:]
        else:
            self.board = [' '] * 9

    def available_moves(self):
        return [i for i in range(9) if self.board[i] == ' ']

    def make_move(self, move, player):
        self.board[move] = player

    def undo_move(self, move):
        self.board[move] = ' '

    def winner(self):

        winning_combinations = [
            [0,1,2],
            [3,4,5],
            [6,7,8],
            [0,3,6],
            [1,4,7],
            [2,5,8],
            [0,4,8],
            [2,4,6]
        ]

        for combo in winning_combinations:
            a,b,c = combo

            if (
                self.board[a] ==
                self.board[b] ==
                self.board[c] != ' '
            ):
                return self.board[a]

        if ' ' not in self.board:
            return "Draw"

        return None

    def display(self):

        print()

        for i in range(0,9,3):
            print(
                self.board[i], "|",
                self.board[i+1], "|",
                self.board[i+2]
            )

        print()


def minimax(game, maximizing):

    result = game.winner()

    if result == 'X':
        return 1

    if result == 'O':
        return -1

    if result == "Draw":
        return 0

    if maximizing:

        best = -math.inf

        for move in game.available_moves():

            game.make_move(move,'X')

            score = minimax(game,False)

            game.undo_move(move)

            best = max(best,score)

        return best

    else:

        best = math.inf

        for move in game.available_moves():

            game.make_move(move,'O')

            score = minimax(game,True)

            game.undo_move(move)

            best = min(best,score)

        return best


def minimax_best_move(game):

    best_score = -math.inf
    best_move = None

    for move in game.available_moves():

        game.make_move(move,'X')

        score = minimax(game,False)

        game.undo_move(move)

        if score > best_score:
            best_score = score
            best_move = move

    return best_move


def alpha_beta(game, alpha, beta, maximizing):

    result = game.winner()

    if result == 'X':
        return 1

    if result == 'O':
        return -1

    if result == "Draw":
        return 0

    if maximizing:

        value = -math.inf

        for move in game.available_moves():

            game.make_move(move,'X')

            value = max(
                value,
                alpha_beta(
                    game,
                    alpha,
                    beta,
                    False
                )
            )

            game.undo_move(move)

            alpha = max(alpha,value)

            if alpha >= beta:
                break

        return value

    else:

        value = math.inf

        for move in game.available_moves():

            game.make_move(move,'O')

            value = min(
                value,
                alpha_beta(
                    game,
                    alpha,
                    beta,
                    True
                )
            )

            game.undo_move(move)

            beta = min(beta,value)

            if alpha >= beta:
                break

        return value


def alpha_beta_best_move(game):

    best_score = -math.inf
    best_move = None

    for move in game.available_moves():

        game.make_move(move,'X')

        score = alpha_beta(
            game,
            -math.inf,
            math.inf,
            False
        )

        game.undo_move(move)

        if score > best_score:
            best_score = score
            best_move = move

    return best_move


def heuristic(game):

    score = 0

    lines = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ]

    for line in lines:

        values = [game.board[i] for i in line]

        x_count = values.count('X')
        o_count = values.count('O')

        if x_count > 0 and o_count == 0:
            score += x_count

        elif o_count > 0 and x_count == 0:
            score -= o_count

    return score


def heuristic_alpha_beta(
        game,
        depth,
        alpha,
        beta,
        maximizing):

    result = game.winner()

    if result == 'X':
        return 100

    if result == 'O':
        return -100

    if result == "Draw":
        return 0

    if depth == 0:
        return heuristic(game)

    if maximizing:

        value = -math.inf

        for move in game.available_moves():

            game.make_move(move,'X')

            value = max(
                value,
                heuristic_alpha_beta(
                    game,
                    depth-1,
                    alpha,
                    beta,
                    False
                )
            )

            game.undo_move(move)

            alpha = max(alpha,value)

            if alpha >= beta:
                break

        return value

    else:

        value = math.inf

        for move in game.available_moves():

            game.make_move(move,'O')

            value = min(
                value,
                heuristic_alpha_beta(
                    game,
                    depth-1,
                    alpha,
                    beta,
                    True
                )
            )

            game.undo_move(move)

            beta = min(beta,value)

            if alpha >= beta:
                break

        return value


def heuristic_alpha_beta_best_move(game, depth=4):

    best_score = -math.inf
    best_move = None

    for move in game.available_moves():

        game.make_move(move,'X')

        score = heuristic_alpha_beta(
            game,
            depth,
            -math.inf,
            math.inf,
            False
        )

        game.undo_move(move)

        if score > best_score:
            best_score = score
            best_move = move

    return best_move


def random_playout(game, player):

    current_player = player

    while game.winner() is None:

        move = random.choice(
            game.available_moves()
        )

        game.make_move(
            move,
            current_player
        )

        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'

    result = game.winner()

    if result == 'X':
        return 1

    elif result == 'O':
        return -1

    return 0


def mcts(game, simulations=1000):

    moves = game.available_moves()

    scores = {}

    for move in moves:

        scores[move] = 0

        for _ in range(simulations):

            temp = TicTacToe(
                game.board.copy()
            )

            temp.make_move(move,'X')

            result = random_playout(
                temp,
                'O'
            )

            scores[move] += result

    best_move = max(
        scores,
        key=scores.get
    )

    return best_move


print("\n========== TEST CASE 1 ==========")

game1 = TicTacToe([
    'X','X',' ',
    'O','O',' ',
    ' ',' ',' '
])

game1.display()

print("Minimax Move:",
      minimax_best_move(game1))

print("Alpha-Beta Move:",
      alpha_beta_best_move(game1))

print("Heuristic Alpha-Beta Move:",
      heuristic_alpha_beta_best_move(game1))

print("MCTS Move:",
      mcts(game1,1000))


print("\n========== TEST CASE 2 ==========")

game2 = TicTacToe([
    'O','O',' ',
    'X',' ',' ',
    ' ',' ','X'
])

game2.display()

print("Minimax Move:",
      minimax_best_move(game2))

print("Alpha-Beta Move:",
      alpha_beta_best_move(game2))

print("Heuristic Alpha-Beta Move:",
      heuristic_alpha_beta_best_move(game2))

print("MCTS Move:",
      mcts(game2,1000))


print("\n========== TEST CASE 3 ==========")

game3 = TicTacToe()

game3.display()

print("Minimax Move:",
      minimax_best_move(game3))

print("Alpha-Beta Move:",
      alpha_beta_best_move(game3))

print("Heuristic Alpha-Beta Move:",
      heuristic_alpha_beta_best_move(game3))

print("MCTS Move:",
      mcts(game3,1000))


print("\n========== EXECUTION COMPLETE ==========")
