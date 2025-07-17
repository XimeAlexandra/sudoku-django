from django.shortcuts import render
from django.http import JsonResponse
from .utils import generate_sudoku_board, verify_sudoku_solution
import json

# Paradigma imperativo: Manejo secuencial del estado y rutas
def index(request):
    # Genera un tablero inicial
    board = generate_sudoku_board()
    return render(request, 'sudoku.html', {'board': board})

def new_game(request):
    # Genera un nuevo tablero y lo retorna como JSON para actualización dinámica
    board = generate_sudoku_board()
    return JsonResponse({'board': board})

def verify(request):
    # Verifica la solución enviada por el usuario
    if request.method == 'POST':
        data = json.loads(request.body)
        board = data.get('board')
        is_valid = verify_sudoku_solution(board)
        return JsonResponse({'valid': is_valid})
    return JsonResponse({'error': 'Invalid request'}, status=400)


