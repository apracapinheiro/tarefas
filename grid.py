grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

x, y = 0, 0
linha = []
while y < 6:
    x = 0
    while x < 9:
        linha.append(grid[x][y])
        if x == 8:
            # print(str(linha), end='\n')
            print(''.join(linha))
            linha = []
        x += 1
    y += 1
