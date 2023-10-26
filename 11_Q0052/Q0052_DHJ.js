/**
 * @param {number} n
 * @return {number}
 */
var totalNQueens = function(n) {
    let answer = 0;
    const board = new Array(n).fill(0).map(() => new Array(n).fill(0));

    const isValid = (board, row, col) => {
       //세로축에 놓을 수 있는지 확인
       for (let i = 0; i < row; i++) {
           if (board[i][col] === 1) {
               return false;
           }
       }
        //왼쪽 상단 대각선방향 확인
       for (let i = row, j = col; i >= 0 && j >= 0; i--, j--) {
           if (board[i][j] === 1) {
               return false;
           }
       }
        //오른쪽 상단 대각선 방향 확인
       for (let i = row, j = col; i >= 0 && j < n; i--, j++) {
           if (board[i][j] === 1) {
               return false;
           }
       }
        
        return true;
   }

    const solveNQueens = (board, row) => {
        if (row === n) {
            answer++;
            return;
        }

        for (let col = 0; col < n; col++) {
            if (isValid(board, row, col)) {
                board[row][col] = 1;
                solveNQueens(board, row + 1);
                board[row][col] = 0;
            }
        }
    }

    solveNQueens(board, 0);
    return answer;
};