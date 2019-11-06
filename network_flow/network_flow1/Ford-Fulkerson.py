import numpy as np


def find_path(graph_matrix, s, t):
    num_of_nodes = graph_matrix.shape[0]
    res_list = [s]
    pop_index = [-1]  # the last adjacent nodes that node has explored
    while res_list:
        temp_node = res_list.pop()
        last_index = pop_index.pop()
        for i in range(last_index+1, num_of_nodes):
            if i not in res_list and graph_matrix[temp_node][i] != 0:
                pop_index.append(i)
                res_list.append(temp_node)
                pop_index.append(-1)
                res_list.append(i)
                if i == t:
                    return res_list
                break
    return None


def bottleneck(residual_matrix, flow):
    edge_capacity = []
    for i in range(len(flow)-1):
        start = flow[i]
        end = flow[i+1]
        capacity = residual_matrix[start][end]
        edge_capacity.append(capacity)
    return min(edge_capacity)


def augment(flow, residual_graph, path, graph_matrix):
    new_flow = flow.copy()
    new_residual_graph = residual_graph.copy()

    bottle = bottleneck(residual_graph, path)
    for i in range(len(path)-1):
        start = path[i]
        end = path[i+1]
        if graph_matrix[start][end] > 0:
            new_flow[start][end] = new_flow[start][end] + bottle
            new_residual_graph[start][end] = new_residual_graph[start][end] - bottle
            new_residual_graph[end][start] = new_residual_graph[end][start] + bottle
        else:
            start, end = end, start  # reverse
            new_flow[start][end] = new_flow[start][end] - bottle
            new_residual_graph[start][end] = new_residual_graph[start][end] + bottle
            new_residual_graph[end][start] = new_residual_graph[end][start] - bottle
    return new_flow, new_residual_graph



def Ford_Fuckrson(graph_matrix, s, t):
    flow = np.zeros(shape=graph_matrix.shape)
    residual_graph = graph_matrix.copy()
    while True:
        path = find_path(residual_graph, s, t)
        if not path:
            return flow
        else:
            flow, residual_graph = augment(flow, residual_graph, path,  graph_matrix)
        # print("path:")
        # print(path)
        # print("flow:")
        # print(flow)
        # print("residual graph:")
        # print(residual_graph)
        # print()


graph_matrix = np.array(
    [[0, 10, 0, 10, 0, 0],
     [0, 0, 4, 2, 8, 0],
     [0, 0, 0, 0, 0, 10],
     [0, 0, 0, 0, 9, 0],
     [0, 0, 6, 0, 0, 10],
     [0, 0, 0, 0, 0, 0]]
)
print(graph_matrix)
flow = Ford_Fuckrson(graph_matrix, 0, 5)
print(flow)
