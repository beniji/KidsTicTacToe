import time

COMPUTER_MARK = -1
USER_MARK = 1

cells = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

lines = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(2, 0), (1, 1), (0, 2)],
]

def character(value):
    if value == 1:
        return "X"
    if value == -1:
        return "O"
    return "."

def show_board():
    for row in cells:
        print(character(row[0]) + "\t" + character(row[1]) + "\t" + character(row[2]))
    print()

def get_user_move():
    while True:
        user_move = input("Enter your move (e.g. 11 for middle cell): ")
        if len(user_move) != 2:
            print("Invalid move, you need to enter exactly two characters")
            continue
        row = int(user_move[0])
        col = int(user_move[1])
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid move, row and col must be between 0 and 2")
            continue
        if cells[row][col] != 0:
            print("Cell already taken")
            continue   
        cells[row][col] = USER_MARK
        break

def score_lines():
    scores = {}
    for i in range(8):
        scores[i] = score_line(i)
    return scores

def score_line(line_number):
    coords = lines[line_number]
    score = 0
    for row, col in coords:
        score = score + cells[row][col]
    return score

def find_lines_with_score(scored_lines, desired_score):
    line_numbers = []
    for line_number, score in scored_lines.items():
        if score == desired_score:
            line_numbers.append(line_number)
    return line_numbers

def find_free_cell(line_number):
    coords = lines[line_number]
    for row, col in coords:
        current_value = cells[row][col]
        if current_value == 0:
            return row, col
    return None

def find_best_cell(scored_lines):
    score_priorities = [-2, 2, -1, 1, 0]
    for prio in score_priorities:
        line_numbers = find_lines_with_score(scored_lines, prio)    
        for line_number in line_numbers:
            move = find_free_cell(line_number)
            if move is not None:
                return move
    return 0, 0
    
def play_computer_move(scored_lines):
    row, col = find_best_cell(scored_lines)
    cells[row][col] = COMPUTER_MARK

def any_line_with_score(scored_lines, desired_score):
    return len(find_lines_with_score(scored_lines, desired_score)) > 0

while True:
    show_board()
    get_user_move()
    scored_lines = score_lines()
    if any_line_with_score(scored_lines, 3):
        winner = "player"
        break
    else:
        print()
        show_board()
    print("\nComputer is thinking...\n")
    time.sleep(1.5)
    play_computer_move(scored_lines)
    scored_lines = score_lines()
    if any_line_with_score(scored_lines, -3):
        winner = "computer"
        break

show_board()
if winner == "player":
    print("GAME OVER - YOU WON DUDE!")
else:
    print("GAME OVER - COMPUTER KICKED YO ASS!")
