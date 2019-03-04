import java.util.Scanner;
import java.io.IOException;

class Main {
	
  public static void main(String args[])throws IOException
  {
    int u,v,s;
    Scanner sc=new Scanner(System.in);
    System.out.println("Enter no of vertices for the graph");
    int vertices=sc.nextInt();
    Graph g=new Graph(vertices);
    while(true){
      System.out.println("Enter 1 to add edges");
      System.out.println("Enter 2 to see adjacency list of a vertex");
      System.out.println("Enter 3 to see the traversal");
      System.out.println("Enter 4 to exit");
      System.out.println("Enter you choice");
      int ch=sc.nextInt();
      switch(ch)
      {
       case 1:System.out.println("Enter the 2 vertices to join by an edge");
              u=sc.nextInt();
	      v=sc.nextInt();
	      g.addEdge(u, v);
	      break;
		        
       case 2:System.out.println("Enter the vertex whos adjacency list you want to check");
	      v=sc.nextInt();
	      g.checkAdjacencyList(v);
	      break;
		        
       case 3:System.out.println("Enter the start node");
	      s=sc.nextInt();
	      g.DFS(s);
	      break;
		        
       case 4:sc.close();
	      System.exit(0);
		 
       default:System.out.println("Invalid Input. Try Again!");
      }
     }
  }
}
