from django.shortcuts import render
from django.http import JsonResponse
from .utils import generate_sudoku_board, verify_sudoku_solution
import json

# Paradigma imperativo: flujo paso a paso basado en condiciones y estado

def index(request):
    # Por defecto genera un tablero nivel fácil
    board = generate_sudoku_board('facil')
    return render(request, 'sudoku.html', {'board': board})

def new_game(request):
    # Lee el nivel de dificultad desde la query string (?difficulty=medio)
    difficulty = request.GET.get('difficulty', 'facil')  # por defecto fácil

    # Genera un tablero según la dificultad
    board = generate_sudoku_board(difficulty)

    # Retorna como JSON
    return JsonResponse({'board': board})

def verify(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        board = data.get('board')

        # Verificación imperativa
        is_valid = verify_sudoku_solution(board)

        return JsonResponse({'valid': is_valid})
    
    return JsonResponse({'error': 'Invalid request'}, status=400)


from .utils import solve_sudoku  # importa la función nueva

def solve(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        board = data.get('board')
        solved = solve_sudoku(board)
        if solved:
            return JsonResponse({'solved': solved})
        return JsonResponse({'error': 'No se pudo resolver'}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)
