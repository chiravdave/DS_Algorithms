from collections import deque
from copy import deepcopy

class Graph:
    
    def __init__(self, vertices):
        self.v = []
        #Creating vertices & adjacency list
        self.e = {}
        for i in range(vertices):
            self.v.append(i+1)
            self.e[i+1] = []

    def addEdge(self, v_start, v_end):
        if v_start in self.v:
            if v_end not in self.e[v_start]:
                self.e[v_start].append(v_end)

    def getChildren(self, u):
        return self.e[u]

    def BFS(self, start, goal):
        visited = []
        fringe = deque()
        fringe.append(tuple((start, [])))
        while len(fringe) != 0:
            u,path = fringe.popleft()
            if u == goal:
                print("There is a path between {} and  {}".format(start, goal))
                return path
            visited.append(u)
            for child in self.getChildren(u):
                if child not in fringe:
                    path_to_child = deepcopy(path)
                    path_to_child.append(u)
                    fringe.append(tuple((child,path_to_child)))
        print("There is no path between {} and  {}".format(start, goal))

    def DFS(self, start, goal):
        visited = []
        fringe = deque()
        fringe.append(tuple((start, [])))
        while len(fringe) != 0:
            u,path = fringe.pop()
            if u == goal:
                print("There is a path between {} and  {}".format(start, goal))
                return path
            visited.append(u)
            for child in self.getChildren(u):
                if child not in fringe:
                    path_to_child = deepcopy(path)
                    path_to_child.append(u)
                    fringe.append(tuple((child,path_to_child)))
        print("There is no path between {} and  {}".format(start, goal))
