import threading
matrix = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
[13, 14, 15, 16]]

min_pooled_matrix = []
max_pooled_matrix = []

def min_pooling():
    for i in range(0, 4, 2):
        min_pooled_matrix.append([
            min(matrix[i][j], matrix[i][j+1],
            matrix[i+1][j], matrix[i+1][j+1])
            for j in range(0, 4, 2)
        ])
    print("Min Pooled 2x2 Matrix:", min_pooled_matrix)
    print("Minimum Value:", min(min_pooled_matrix[0] + min_pooled_matrix[1]))

def max_pooling():
    for i in range(0, 4, 2):
        max_pooled_matrix.append([
            max(matrix[i][j], matrix[i][j+1],
            matrix[i+1][j], matrix[i+1][j+1])
            for j in range(0, 4, 2)
        ])
    print("\nMax Pooled 2x2 Matrix:", max_pooled_matrix)
    print("Maximum Value:",
    max(max_pooled_matrix[0] + max_pooled_matrix[1]))

t1 = threading.Thread(target=min_pooling)
t2 = threading.Thread(target=max_pooling)
t1.start()
t2.start()
t1.join()
t2.join()
print("\nAll threads have completed")