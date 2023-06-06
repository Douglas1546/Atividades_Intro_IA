import heapq

class MinHeap:
    def __init__(self):
        self.contents = []
        self.capacity = 0
        self.size = 0

    def remove_min(self):
        if self.size < 1:
            return None 
        
        minimo = self.contents[0]
        self.contents[0] = self.contents[self.size-1]
        self.size -= 1

        self.__min_heapify(0)

        return minimo

    def adiciona(self, node):
        indice = self.size 
        if self.capacity == self.size:
            self.contents.append(node)
            self.capacity += 1
        self.__insert(indice, node)
        self.size += 1

    def __pai(self, i):
        return (i - 1) // 2

    def __filho_esquerdo(self, i):
        return i * 2 + 1

    def __filho_direito(self, i):
        return i * 2 + 2

    def __swap(self, i, j):
        self.contents[i], self.contents[j] = self.contents[j], self.contents[i]

    def __min_heapify(self, i):
        l = self.__filho_esquerdo(i)
        r = self.__filho_direito(i)

        minimo = i 

        if l < self.size and self.contents[i].f > self.contents[l].f:
            minimo = l 

        if r < self.size and self.contents[minimo].f > self.contents[r].f:
            minimo = r 

        if minimo != i:
            self.__swap(i, minimo)
            self.__min_heapify(minimo)

    def __insert(self, i, node):
        self.contents[i] = node 
        while i > 0 and self.contents[self.__pai(i)].f > self.contents[i].f:
            self.__swap(i, self.__pai(i))
            i = self.__pai(i)


class PriorityQueue:
    def __init__(self):
        self.heap = MinHeap()

    def remove_min(self):
        return self.heap.remove_min()

    def adiciona(self, node):
        self.heap.adiciona(node)


class Node:
    def __init__(self, state, parent=None, action=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.g = g
        self.h = h

    @property
    def f(self):
        return self.g + self.h

    def __lt__(self, other):
        return self.f < other.f

def a_star(graph, start, goal, heuristic):
    priority_queue = []
    start_node = Node(start, g=0, h=heuristic[start])
    heapq.heappush(priority_queue, (0, start_node)) # Passo 1

    while priority_queue: # Passo 2
        _, current_node = heapq.heappop(priority_queue)# Passo 3

        if current_node.state == goal: # Passo 4
            return build_path(current_node)

        for neighbor, cost in graph[current_node.state].items(): # Passo 5
            g = current_node.g + cost
            h = heuristic[neighbor]
            neighbor_node = Node(neighbor, parent=current_node, action=None, g=g, h=h)
            heapq.heappush(priority_queue, (g, neighbor_node)) # Passo 6

    return None # Caso o objetivo não seja encontrado


def build_path(node):
    path = []
    current = node
    while current is not None:
        path.append(current.state)
        current = current.parent
    path.reverse()
    return path


# Grafo da Romênia
graph = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101},
}

heuristic = {
    'Arad': 366,
    'Zerind': 374,
    'Oradea': 380,
    'Sibiu': 253,
    'Timisoara': 329,
    'Lugoj': 244,
    'Mehadia': 241,
    'Drobeta': 242,
    'Craiova': 238,
    'Rimnicu Vilcea': 193,
    'Fagaras': 176,
    'Pitesti': 100,
    'Bucharest': 0,
}

path = a_star(graph, 'Arad', 'Bucharest', heuristic)
print("A* Algoritmo com custo e Heuristica:\n")
print("Caminho encontrado:", path)
cost = sum(graph[path[i]][path[i+1]] for i in range(len(path)-1))
print("Custo acumulado:", cost)
print("\n===========================================================================================================================================\n")

path = a_star(graph, 'Timisoara', 'Bucharest', heuristic)
print("A* Algoritmo com custo e Heuristica:\n")
print("Caminho encontrado:", path)
cost = sum(graph[path[i]][path[i+1]] for i in range(len(path)-1))
print("Custo acumulado:", cost)
print("\n===========================================================================================================================================\n")

path = a_star(graph, 'Craiova', 'Bucharest', heuristic)
print("A* Algoritmo com custo e Heuristica:\n")
print("Caminho encontrado:", path)
cost = sum(graph[path[i]][path[i+1]] for i in range(len(path)-1))
print("Custo acumulado:", cost)
print("\n===========================================================================================================================================\n")