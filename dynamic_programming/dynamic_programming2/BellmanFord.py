import numpy as np


graph_matrix = np.array(
    [[ 0,  5,  0,  0,  9, 0,  0,  8],
 [ 0,  0,  12,  -3,  0,  0,  0,  4],
 [ 0,  0,  0,  -5, 0,  0,  11,  0],
 [ 0,  0,  0,  0,  0,  0,  9,  0],
 [ 0,  0,  0,  0,  0,  -3,  10,  5],
 [ 0,  0,  1,  0,  0,  0,  13,  0],
 [ 0,  0,  0,  0,  0,  0,  0,  0],
 [ 0,  0,  7,  0,  0,  -1,  0,  0]])
print(graph_matrix)

def shortest_path(graph_matrix,  target):
    node_num = graph_matrix.shape[0]
    opt_matrix = np.zeros(shape=(node_num, node_num))
    # opt(i,v) cost of shortest v-t path that uses \le i edges
    for i in range(node_num):
        opt_matrix[0][i] = 100
    opt_matrix[0][target] = 0
    for length in range(1, node_num):
        for node in range(node_num):
            opt_matrix[length][node] = opt_matrix[length-1][node]
            for endpoint in range(node_num):
                value = graph_matrix[node][endpoint]
                if value != 0:
                    opt_w = opt_matrix[length - 1, endpoint]
                    if opt_w != 100:  # exist path from w to tail
                        new_value = opt_w + value
                        opt_matrix[length][node] = min(opt_matrix[length][node], new_value)
    print(opt_matrix)

def Bellman_fold(graph_matrix, target):
    node_num = graph_matrix.shape[0]
    d = np.zeros(shape=(node_num, 1))
    successor = np.ndarray(shape=(node_num, 1))
    for i in range(node_num):
        successor[i] = -1  # null
        d[i] = 100  # positive infinity
    d[target] = 0
    update = [True] * node_num
    for length in range(1, node_num):
        update_new = [False] * node_num
        for w in range(node_num):
            if update[w]:
                update[w] = False
                for v in range(node_num):
                    value = graph_matrix[v][w]
                    if value != 0 and d[w] != 100 and d[v] > d[w] + value:
                        d[v] = d[w] + value
                        update_new[v] = True
                        successor[v] = w
        update = update_new[:]
        if True not in update:
            break
    print(d.transpose())
    print(successor.transpose())


shortest_path(graph_matrix, 6)
Bellman_fold(graph_matrix, 6)
