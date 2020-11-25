import os
def flippingMatrix(matrix):
    l=len(matrix)
    Max=0
    for i in range (l//2):
        for j in range(l//2):
            Max+=max(matrix[i][j],matrix[i][l-j-1],matrix[l-i-1][j],matrix[l-i-1][l-j-1])
    return Max
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        matrix = []

        for _ in range(2*n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
