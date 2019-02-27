from graph import Graph

def main():
    vertices = int(input("Enter no of vertices"))
    graph = Graph(vertices)
    print("Enter 1 to add edge, 2 for BFS search, 3 for DFS search and 4 to exit")
    while(True):
        choice = input("Enter your choice")
        if choice == "1":
            print("Enter the start and end vertices")
            start = int(input())
            end = int(input())
            graph.addEdge(start, end)
        elif choice == "2":
            print("Enter the start and end vertices")
            start = int(input())
            end = int(input())
            path = graph.BFS(start, end)
            print(path)
        elif choice == "3":
            print("Enter the start and end vertices")
            start = int(input())
            end = int(input())
            path = graph.DFS(start, end)
            print(path)
        elif choice == "4":
            return

if __name__ == "__main__":
    main()
