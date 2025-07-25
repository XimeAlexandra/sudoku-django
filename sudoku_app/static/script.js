window.newGame = async function () {
    const difficulty = document.getElementById("difficulty").value;

    const response = await fetch(`/new_game?difficulty=${difficulty}`, {
        method: "GET",
    });

    const data = await response.json();
    updateBoard(data.board);
};


async function verifySolution() {
    const board = getBoardState();
    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
    const response = await fetch('/verify', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({ board })
    });
    const data = await response.json();

    const resultEl = document.getElementById('result');

    if (data.valid) {
        alert('✅ ¡La solución es válida!');
        resultEl.innerText = '✅ ¡Solución correcta!';
        resultEl.style.color = 'green';
    } else {
        alert('❌ La solución es incorrecta.');
        resultEl.innerText = '❌ Solución incorrecta.';
        resultEl.style.color = 'red';
    }
}

function getBoardState() {
    const cells = document.querySelectorAll('.cell');
    const board = [];
    let row = [];
    cells.forEach((cell, index) => {
        row.push(cell.value ? parseInt(cell.value) : 0);
        if ((index + 1) % 9 === 0) {
            board.push(row);
            row = [];
        }
    });
    return board;
}

function updateBoard(board) {
    const cells = document.querySelectorAll('.cell');
    cells.forEach((cell, index) => {
        const row = Math.floor(index / 9);
        const col = index % 9;
        const value = board[row][col];
        cell.value = value !== 0 ? value : '';
        cell.readOnly = value !== 0;
    });
    document.getElementById('result').innerText = '';
    document.getElementById('result').style.color = 'black';
}

window.solveSudoku = async function () {
    const board = getBoardState();

    const response = await fetch('/solve', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.querySelector('meta[name="csrf-token"]').getAttribute('content'),
        },
        body: JSON.stringify({ board }),
    });

    const data = await response.json();

    if (data.solved) {
        const solvedBoard = data.solved;
        const inputs = document.querySelectorAll('#sudoku-board input');
        inputs.forEach((input, index) => {
            const row = Math.floor(index / 9);
            const col = index % 9;
            input.value = solvedBoard[row][col];
            input.readOnly = true;
            input.classList.add('solved-cell'); 
        });
    } else {
        alert('No se pudo resolver el Sudoku.');
    }
};
