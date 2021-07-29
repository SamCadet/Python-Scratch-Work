grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# https://stackoverflow.com/questions/30424355/automate-the-boring-stuff-with-python-chapter-4-exercise

# The zip(*grid) effectively transposes the matrix (flip it on the main diagonal), then each row is joined into one string,
# then the rows are joined with newlines so the whole thing can be printed at once.

# print('\n'.join(map(''.join, zip(*grid))))


# Using only what the book had covered, and keeping in mind the loop within a loop hint, this is my answer:

for j in range(len(grid[0])):
    for i in range(len(grid)):
        print(grid[i][j], end='')
    print()
