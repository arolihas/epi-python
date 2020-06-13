def rotate_matrix(matrix):
    size = len(matrix) - 1
    for i in range(len(matrix) // 2):
        for j in range(i, size - i):
            ni = -(i+1)
            nj = -(j+1)
            matrix[i][j], matrix[nj][i], matrix[ni][nj], matrix[ni][j] =
            matrix[nj][i], matrix[ni][nj], matrix[j][ni], matrix[i][j]

