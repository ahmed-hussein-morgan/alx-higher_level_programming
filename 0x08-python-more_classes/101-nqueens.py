#!/usr/bin/python3
import sys
"""queen"""
def solve_n_queens(n):
    """queen"""
    def can_place(pos, ocuppied_rows):
        """queen"""
        for i in range(ocuppied_rows):
            if pos[i] == pos[ocuppied_rows] or \
                pos[i] - pos[ocuppied_rows] == ocuppied_rows - i or \
                pos[i] - pos[ocuppied_rows] == i - ocuppied_rows:
                return False
        return True

    def place_queen(n, index, positions):
        """queen"""
        if index == n:
            result.append(list(positions))
            return
        for i in range(n):
            positions.append(i)
            if can_place(positions, index):
                place_queen(n, index + 1, positions)
            positions.pop()

    result = []
    place_queen(n, 0, [])
    return result

def main():
    """queen"""
    if len(sys.argv) != 2 or not sys.argv[1].isdigit() or int(sys.argv[1]) < 4:
        print('Usage: nqueens N')
        print('where N must be an integer greater or equal to 4')
        sys.exit(1)
    n = int(sys.argv[1])
    solutions = solve_n_queens(n)
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()
