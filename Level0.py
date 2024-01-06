import json

fh=open("level0.json")

data=json.load(fh)

fh.close()

adj=[]
for i in data["neighbourhoods"]:
    adj.append(data["neighbourhoods"][i]["distances"])

N=len(adj)

def nearest_neighbor(adjacency_matrix,ind):
    num_cities = len(adjacency_matrix)
    unvisited_cities = set(range(0, num_cities))

    tour = [ind]  
    unvisited_cities.remove(ind)

    while unvisited_cities:
        current_city = tour[-1]
        nearest_city = min(unvisited_cities, key=lambda city: adjacency_matrix[current_city][city])
        tour.append(nearest_city)
        unvisited_cities.remove(nearest_city)

    
    tour.append(tour[0])

    return tour

def calculate_tour_distance(tour, adjacency_matrix):
    distance = 0
    for i in range(len(tour) - 1):
        distance += adjacency_matrix[tour[i]][tour[i + 1]]
    return distance


adj_matrix = [[0, 3366, 2290, 3118, 1345, 854, 1176, 1291, 1707, 2160, 1606, 702, 1820, 1985, 1838, 1515, 3370, 1643, 2874, 1418], [3366, 0, 1076, 512, 2021, 2512, 2190, 2075, 1923, 1206, 1760, 2664, 1546, 1645, 1528, 1851, 376, 1723, 492, 1948], [2290, 1076, 0, 1494, 945, 1436, 1114, 999, 2905, 536, 684, 1588, 876, 2627, 452, 775, 1358, 647, 716, 872], [3118, 512, 1494, 0, 1773, 2264, 1942, 1827, 1411, 958, 1512, 2416, 1298, 1133, 1280, 1603, 252, 1475, 778, 1700], [1345, 2021, 945, 1773, 0, 491, 403, 650, 2348, 815, 261, 787, 475, 2070, 493, 170, 2025, 298, 1529, 763], [854, 2512, 1436, 2264, 491, 0, 322, 569, 2429, 1306, 752, 868, 966, 2151, 984, 661, 2516, 789, 2020, 682], [1176, 2190, 1114, 1942, 403, 322, 0, 247, 2751, 984, 430, 1190, 722, 2473, 662, 521, 2194, 467, 1698, 360], [1291, 2075, 999, 1827, 650, 569, 247, 0, 2998, 869, 677, 1437, 969, 2720, 547, 768, 2079, 352, 1583, 127], [1707, 1923, 2905, 1411, 2348, 2429, 2751, 2998, 0, 2369, 2321, 1561, 2029, 278, 2553, 2230, 1663, 2646, 2189, 3111], [2160, 1206, 536, 958, 815, 1306, 984, 869, 2369, 0, 554, 1458, 340, 2091, 322, 645, 1210, 517, 714, 742], [1606, 1760, 684, 1512, 261, 752, 430, 677, 2321, 554, 0, 904, 292, 2043, 232, 91, 1764, 325, 1268, 790], [702, 2664, 1588, 2416, 787, 868, 1190, 1437, 1561, 1458, 904, 0, 1118, 1283, 1136, 813, 2668, 1085, 2172, 1550], [1820, 1546, 876, 1298, 475, 966, 722, 969, 2029, 340, 292, 1118, 0, 1751, 524, 305, 1550, 617, 1054, 1082], [1985, 1645, 2627, 1133, 2070, 2151, 2473, 2720, 278, 2091, 2043, 1283, 1751, 0, 2275, 1952, 1385, 2368, 1911, 2833], [1838, 1528, 452, 1280, 493, 984, 662, 547, 2553, 322, 232, 1136, 524, 2275, 0, 323, 1532, 195, 1036, 558], [1515, 1851, 775, 1603, 170, 661, 521, 768, 2230, 645, 91, 813, 305, 1952, 323, 0, 1855, 416, 1359, 881], [3370, 376, 1358, 252, 2025, 2516, 2194, 2079, 1663, 1210, 1764, 2668, 1550, 1385, 1532, 1855, 0, 1727, 642, 1952], [1643, 1723, 647, 1475, 298, 789, 467, 352, 2646, 517, 325, 1085, 617, 2368, 195, 416, 1727, 0, 1231, 465], [2874, 492, 716, 778, 1529, 2020, 1698, 1583, 2189, 714, 1268, 2172, 1054, 1911, 1036, 1359, 642, 1231, 0, 1456], [1418, 1948, 872, 1700, 763, 682, 360, 127, 3111, 742, 790, 1550, 1082, 2833, 558, 881, 1952, 465, 1456, 0]]

r0= data["restaurants"]['r0']['neighbourhood_distance']
startVal=min(r0)
ind=r0.index(startVal)
#ind=4
result_tour = nearest_neighbor(adj_matrix,ind)
result_tour.pop()

print(ind)
min_distance = calculate_tour_distance(result_tour, adj_matrix)
min_distance= min_distance + r0[result_tour[0]] + r0[result_tour[-1]]
print("Nearest Neighbor Tour:", result_tour)
print("Minimum Tour Distance:", min_distance)

for i in range(len(result_tour)):
    result_tour[i]="n"+str(result_tour[i]+1)

result_tour.insert(0,"r0")
result_tour.append("r0")
print(result_tour)
dict1={}
dict={}
dict1["path"]=result_tour
dict["v0"]=dict1

print(dict)


fh=open("level0_output.json", "w")

data=json.dump(dict,fh)

fh.close()