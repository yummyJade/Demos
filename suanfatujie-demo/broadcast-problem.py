

# 一次次查找覆盖最大的洲

# 创建一个列表，传入set，得到集合，好处就是不重复

states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id","mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set()

while states_needed:

    best_station = None
    states_covered = set() # 所有未覆盖的洲-->应该注解有误，指的应该是已经覆盖的内容吧
    for station, states in stations.items():
        covered = states_needed & states      # 计算交集，当前广播台 还未覆盖的洲
        if len(covered) > len(states_covered):   # ？？？
            best_station = station
            states_covered = covered
        
        states_needed -= states_covered
        final_stations.add(best_station)



print(final_stations)

