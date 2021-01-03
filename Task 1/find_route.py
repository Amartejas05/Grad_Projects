#Amartejas Manjunath
#1001742606

import sys
from queue import PriorityQueue

class node:
    def __init__(self, cost, present_state):
        self.cost = cost
        self.present_state = present_state

    def __lt__(self, other):
        return self.cost < other.cost

ifile = sys.argv[1]
acity = sys.argv[2]
bcity = sys.argv[3]

da = []
closed_set = set()
maxnodes = 0
node_gen = 0
curr = 0
nodes_exp = 0
count = 0
inp = str(ifile)

try:
    a = open(inp, "r+")
    data = ""
    while data != "END OF INPUT":
        data = a.readline()
        da.append(data)
    a.close()
except:
    print("No Input file found")

parent_node = node(0, acity)
q = PriorityQueue(maxsize=80)
q.put(parent_node)
count+=1
fringe_length = q.qsize()
goal = None

while not(q.qsize() == 0) and goal is None:
    curr = q.get()
    node_gen+= 1
    if maxnodes < q.qsize():
        maxnodes = q.qsize()
    if curr.present_state == bcity:
        goal = curr
        break
    else:
        if curr.present_state not in closed_set:
            closed_set.add(curr.present_state)
            for i in da:
                if curr.present_state in i:
                    ans = i
                    c1, c2, fcost = ans.split(" ")
                    fcost = float(fcost)
                    if c1 == curr.present_state:
                        city = node(curr.cost + fcost, c2)
                        q.put(city)
                        nodes_exp += 1
                    else:
                        city = node(curr.cost + fcost, c1)
                        q.put(city)
                        nodes_exp += 1


if goal == None:
    print("Distance: Infinity")
    print("nodes Expanded:", node_gen)
    print("nodes Generated:", nodes_exp)
    print("Maximum nodes in Memory:", maxnodes+1)
    exit()

print("nodes Expanded:", node_gen)
print("nodes Generated:", nodes_exp)
print("Distance:", goal.cost, "kms")
print("Maximim nodes in Memory:", maxnodes+1)
