# Using the "python-chess" library
# pip install python-chess
import chess

# A constant value for the depth of Min-Max tree
DEPTH = 4


# Starting the Min-Max algorithm
def minimaxRoot(depth, board, maximizer):
    # A set of legal moves
    possibleMoves = board.legal_moves
    # Best move score is set to negative infinity (-9999)
    bestMove = -9999
    secondBest = -9999
    thirdBest = -9999
    bestMoveFinal = None

    # Iterating through possible moves
    for x in possibleMoves:
        move = chess.Move.from_uci(str(x))
        board.push(move)
        value = max(bestMove, minimax(depth - 1, board, not maximizer))
        board.pop()
        # Checking if we have found a better move
        if value > bestMove:
            print('Best score: ', str(bestMove))
            print('Best move: ', str(bestMoveFinal))
            print('Second best: ', str(secondBest))
            thirdBest = secondBest
            secondBest = bestMove
            bestMove = value
            bestMoveFinal = move
    return bestMoveFinal


# Continue doing Min-Max algorithm
def minimax(depth, board, is_maximizing):
    if depth == 0:
        return -evaluation(board)
    # A set of legal moves
    possibleMoves = board.legal_moves

    # Max player
    if is_maximizing:
        bestMove = -9999
        # Iterating through possible moves
        for x in possibleMoves:
            move = chess.Move.from_uci(str(x))
            board.push(move)
            bestMove = max(bestMove, minimax(depth - 1, board, not is_maximizing))
            board.pop()
        return bestMove
    # Min player
    else:
        bestMove = 9999
        # Iterating through possible moves
        for x in possibleMoves:
            move = chess.Move.from_uci(str(x))
            board.push(move)
            bestMove = min(bestMove, minimax(depth - 1, board, not is_maximizing))
            board.pop()
        return bestMove


# Evaluation function (heuristic)
def evaluation(board):
    i = 0
    evaluation = 0
    x = True
    try:
        x = bool(board.piece_at(i).color)
    except AttributeError as error:
        x = x
    while i < 63:
        i += 1
        evaluation = evaluation + (
            getPieceValue(str(board.piece_at(i))) if x else -getPieceValue(str(board.piece_at(i))))
    return evaluation


# Setting an abstract value for each piece
def getPieceValue(piece):
    if piece is None:
        return 0
    value = 0
    if piece == 'P' or piece == 'p':
        value = 10
    if piece == 'N' or piece == 'n':
        value = 30
    if piece == 'B' or piece == 'b':
        value = 30
    if piece == 'R' or piece == 'r':
        value = 50
    if piece == 'Q' or piece == 'q':
        value = 90
    if piece == 'K' or piece == 'k':
        value = 900
    # value = value if (board.piece_at(place)).color else -value
    return value


# Driver code
def main():
    board = chess.Board()
    n = 0
    print(board)
    while n < 100:
        # Player turn
        if n % 2 == 0:
            while True:
                # Taking input until a valid input is entered
                try:
                    move = input('Enter move: ')
                    move = chess.Move.from_uci(str(move))
                    # Legality check
                    if move in board.legal_moves:
                        board.push(move)
                        break
                    else:
                        print('Illegal move!')
                except:
                    print('Invalid input!')
        # Computer turn
        else:
            print('Computers Turn:')
            move = minimaxRoot(DEPTH, board, True)
            move = chess.Move.from_uci(str(move))
            board.push(move)
        print(board)
        n += 1


# Execution
if __name__ == '__main__':
    main()
