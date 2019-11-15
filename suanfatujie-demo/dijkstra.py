
# 迪杰斯特拉
graph = {}

graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

# 表示无穷大
infinity = float("inf")

# 关于开销表，就是过来这个点所需花费

costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity


# 关于父节点(这个目的何在)  寻路用
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# 记录处理过的节点
processed = []

node = find_lowest_cost_node(costs)     # 在未处理的节点中找到开销最小的
while node is not None:
    costs = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():      # 遍历所有的邻居
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node

    processed.append(node)
    node = find_lowest_cost_node(costs)


def find_lowest_cost_node():

    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost && node not in processed:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node

