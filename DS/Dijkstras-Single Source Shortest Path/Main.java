import java.util.Scanner;

class Main {

   public static void main(String[] args) {
     int u,v,s=0,w;
     Scanner sc=new Scanner(System.in);
     System.out.println("Enter no of vertices for the graph");
     int vertices=sc.nextInt();
     Graph g=new Graph(vertices);
     while(true){
	System.out.println("Enter 1 to add edges");
	System.out.println("Enter 2 to find the single source shortest path");
	System.out.println("Enter 3 to find the shortest path to a particular vertex(Make sure you have constructed DJK by choosing option 2)");  
	System.out.println("Enter 4 to exit");
	System.out.println("Enter you choice");
	int ch=sc.nextInt();
	switch(ch)
	{
	 case 1:System.out.println("Enter the 2 vertices to join by an edge and its weight");
		u=sc.nextInt();
		v=sc.nextInt();
		w=sc.nextInt();
		g.addEdge(u,v,w);
		break;
			        
	 case 2:System.out.println("Enter the start node");
		s=sc.nextInt();
		g.constructDJK(s);
		break;
			
	case 3:System.out.println("Enter the end node");
	       int e=sc.nextInt();
	       g.showPath(s,e);
	       break;
			       			        
	case 4: sc.close();
	        System.exit(0);
			 
        default:System.out.println("Invalid Input. Try Again!");
	}
     }
   }
}
