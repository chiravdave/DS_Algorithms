import java.util.Iterator;
import java.util.LinkedList;

public class Graph {

  private int v;//no of vertices 
  private LinkedList<Integer> e[];//to store adjacency list(edges) of all the vertices
  
  //Initializing the graph
  Graph(int v)
  {
    this.v=v;
    e=new LinkedList[v];
    for(int i=1;i<=v;i++)
     e[i-1]=new LinkedList<Integer>();// any vertex i will be represented by i-1 index value 
  }
  
  //Function to add an edge between 2 vertices
  void addEdge(int u,int v)
  {
    e[u-1].add(v-1);// any vertex x will be represented by x-1 index value
  }
  
  //print BFS travel from any starting node
  void BFS(int s)
  {
    LinkedList<Integer> queue=new LinkedList<Integer>();//Queue for BFS
    boolean visit[]=new boolean[v];//To check if a vertex has been visited or not
    visit[s-1]=true;//Marking the starting node as visited
    queue.add(s);
    System.out.println("BFS Traversal Begins:\n"+s);
    while(!queue.isEmpty())
    {
      int u=queue.removeFirst();//Remove the head of the queue
      Iterator<Integer> i=e[u-1].listIterator();//Traversing adjacency list of the vertex u
      while(i.hasNext())
      {
	int v=i.next();
	if(visit[v]==false)//checking if the current vertex is not visited 
	{
	 visit[v]=true;
	 System.out.println(v+1);
	 queue.add(v+1);
	}
      }
     }
   System.out.println("Traversal Completed");
  }
  
  void checkAdjacencyList(int v)
  {
    Iterator<Integer> i=e[v-1].listIterator();//Traversing adjacency list of the vertex u
    while(i.hasNext())
    {
     System.out.println((i.next()+1)+"\t");
    }
  }
}
