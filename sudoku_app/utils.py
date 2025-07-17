import random
from copy import deepcopy

# Paradigma funcional: Generación de tablero con funciones puras
def generate_sudoku_board():
    def create_empty_board():
        return [[0] * 9 for _ in range(9)]
    
    def is_valid(board, row, col, num):
        # Verifica si un número puede colocarse en la posición (row, col)
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if board[i][j] == num:
                    return False
        return True
    
    def fill_board(board):
        # Función recursiva pura para llenar el tablero
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    numbers = list(range(1, 10))
                    random.shuffle(numbers)
                    for num in numbers:
                        if is_valid(board, i, j, num):
                            board[i][j] = num
                            if fill_board(board):
                                return board
                            board[i][j] = 0
                    return None
        return board
    
    def remove_numbers(board, holes=40):
        # Crea una copia del tablero y elimina números aleatoriamente
        new_board = deepcopy(board)
        positions = [(i, j) for i in range(9) for j in range(9)]
        random.shuffle(positions)
        for i, (row, col) in enumerate(positions[:holes]):
            new_board[row][col] = 0
        return new_board
    
    # Genera un tablero completo y luego elimina números
    board = create_empty_board()
    filled_board = fill_board(board)
    return remove_numbers(filled_board)

# Paradigma lógico: Verificación del tablero con reglas lógicas
def verify_sudoku_solution(board):
    def check_row(row):
        nums = [x for x in board[row] if x != 0]
        return len(nums) == len(set(nums))
    
    def check_col(col):
        nums = [board[i][col] for i in range(9) if board[i][col] != 0]
        return len(nums) == len(set(nums))
    
    def check_box(box_row, box_col):
        nums = []
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if board[i][j] != 0:
                    nums.append(board[i][j])
        return len(nums) == len(set(nums))
    
    # Verifica todas las reglas del Sudoku
    for i in range(9):
        if not check_row(i) or not check_col(i):
            return False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not check_box(i, j):
                return False
    return True

def verify_sudoku_solution(board):
    def check_row(row):
        nums = [x for x in board[row] if x != 0]
        return len(nums) == len(set(nums))
    
    def check_col(col):
        nums = [board[i][col] for i in range(9) if board[i][col] != 0]
        return len(nums) == len(set(nums))
    
    def check_box(box_row, box_col):
        nums = []
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if board[i][j] != 0:
                    nums.append(board[i][j])
        return len(nums) == len(set(nums))
    
    # Verifica todas las reglas del Sudoku
    for i in range(9):
        if not check_row(i) or not check_col(i):
            return False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not check_box(i, j):
                return False

    # NUEVA CONDICIÓN: el tablero debe estar lleno
    for row in board:
        if 0 in row:
            return False

    return True
