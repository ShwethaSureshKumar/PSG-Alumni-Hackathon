import json

def nearest_neighbor(adjacency_matrix,ind):
    print("------------------")
    print(adjacency_matrix)
    print(len(adjacency_matrix))
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

fh=open("level1a.json")

data=json.load(fh)

fh.close()


adj=[]
for i in data["neighbourhoods"]:
    adj.append(data["neighbourhoods"][i]["distances"])
    print(i)
N=len(adj)


adj_matrix = adj
r0= data["restaurants"]['r0']['neighbourhood_distance']
startVal=min(r0)
ind=r0.index(startVal)
#ind=4
result_tour = nearest_neighbor(adj_matrix,ind)
result_tour.pop()

"""print(ind)
min_distance = calculate_tour_distance(result_tour, adj_matrix)
min_distance= min_distance + r0[result_tour[0]] + r0[result_tour[-1]]
print("Nearest Neighbor Tour:", result_tour)
print("Minimum Tour Distance:", min_distance)"""

costList=[]
for i in data["neighbourhoods"]:
    costList.append(data["neighbourhoods"][i]["order_quantity"])

cap=data["vehicles"]["v0"]["capacity"]
costsum=0
path=[]
index=[]
i=0
while any(costList):
    if costList[i]+costsum <= cap:
        costsum+=costList[i]
        costList[i]=0
        index.append(result_tour[i])
        i+=1
    else:
        path.append(index)
        costsum=0
        index=[]

print(path)

totalcost=0
path[-1].pop()
for tour in path:
    stour=tour

    min_distance = calculate_tour_distance(stour, adj_matrix) 
    totalcost+=min_distance
    print(tour,min_distance)

path[-1].append(3)
print("Total cost:",totalcost)

for i in range(len(path)):
     for k in range(len(path[i])):
          path[i][k]="n"+str(path[i][k])
     path[i].insert(0,"r0")
     path[i].append("r0")

print(path)


dict={}
dict1={}
for i in range(len(path)):
     dict1["path"+str(i+1)]=path[i]
    
dict["v0"]=dict1

print(dict)


fh=open("level1a_output.json", "w")

data=json.dump(dict,fh)

fh.close()

"""
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


fh=open("level1_output.json", "w")

data=json.dump(dict,fh)

fh.close()"""