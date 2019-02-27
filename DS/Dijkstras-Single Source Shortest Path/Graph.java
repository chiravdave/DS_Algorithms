import java.util.ArrayList;
import java.util.Iterator;
import java.util.LinkedList;

class Edge{
  private int dest,weight;
  Edge(int dest,int weight){
	  this.dest=dest;
	  this.weight=weight;
  }
  int getDest(){
	  return dest;
  }
  int getWeight(){
	  return weight;
  }
}

public class Graph {
	private int vertices;
	int parent[],distance[];
	LinkedList<Edge> e[];//to store adjacency list(edges) of all the vertices
    Graph(int v)
	 {
	  vertices=v;
	  e=new LinkedList[v];
	  for(int i=0;i<vertices;i++)
	  e[i]=new LinkedList<Edge>();
	  }	  
	  //Function to add an edge between 2 vertices
	  void addEdge(int u,int v,int weight)
	  {
		  e[u].add(new Edge(v,weight));
	  }
	  
	  void constructDJK(int s){
		  parent=new int[vertices]; // For storing parents of each vertices
		  distance=new int[vertices];// To store distances of vertices from source
		  int key[]=new int[vertices];//Key to be provided to the priority queue  
		  boolean visited[]=new boolean[vertices];//to mark if a vertex is visites or not
		  ArrayList<Integer> queue=new ArrayList<Integer>();        
		  for(int i=0;i<vertices;i++){
			  parent[i]=-1;//no parent initially
			  distance[i]=key[i]=Integer.MAX_VALUE;//Infinity initially
			  visited[i]=false;
		  }
		  distance[s]=key[s]=0;//distance of source from itself is 0
		  visited[s]=true;
		  PriorityQueue pq=new PriorityQueue(key);
		  queue.add(s);
		  while(!queue.isEmpty()){ //run until all vertices are explored
	    	int u;
			int min=pq.extractMin();
			for(u=0;u<vertices;u++){//to get the exact node with minimum key returned
				if(distance[u]==min)
					break;
			}
			queue.remove((Object)u);
      		Iterator<Edge> it=e[u].listIterator();//Traversing adjacency list of the vertex u
			while(it.hasNext())
			{
				Edge e=it.next();
				int v=e.getDest();
				int dist=distance[u]+e.getWeight();
				if(dist<distance[v]){ //update the shortest path to reach v-vertex
					pq.updateKey(distance[v],dist);
					distance[v]=dist;
					parent[v]=u;
				}
				if(visited[v]==false)
				{
					queue.add(v);
					visited[v]=true;
				}
		  }			  
	  }
	}
	private int show(int start,int end){
		 if(end==start){
			 System.out.print("The path is as follows:\n"+start);
			 return 1;}
		 else if(parent[end]==-1){
		     System.out.println("There is no path");
		      return -1;
		     }
	     else{
			 show(start,parent[end]);
			 System.out.print("-->"+end);
			 return 1;
            }
  }
	void showPath(int start,int end){
		int check=show(start,end);
		if(check==1)
		System.out.println("\nDistance is "+distance[end]);		
	}
}

class PriorityQueue{
	int key[],size;
	
	PriorityQueue(int []key){
		this.key=key;
		size=key.length;
		for(int i=size/2-1;i>=0;i--){
		buildMinHeap(i);
		}
	}
	private void buildMinHeap(int i){
		    int left=2*i+1;
			int right=left+1;
			int min=i;
			if(left<size && key[min]>key[left])
				min=left;
			if(right<size && key[min]>key[right])
				min=right;
			if(min!=i){
				swap(min,i);
				buildMinHeap(min);
			}
		}
	int extractMin(){
	  int min=key[0];
	  if(size>1){
	  swap(0,size-1);
	  size--;
	  buildMinHeap(0);}
	  return min;
	}
	private void swap(int x,int y){
		int temp=key[x];
		key[x]=key[y];
		key[y]=temp;
	}
  void updateKey(int oldV,int newV){
	  int i;
	  for(i=0;i<size;i++)//find the index of the key to be updated
	  {
		  if(key[i]==oldV){
			  key[i]=newV;
			  break;
		  }
	  }
	  int j=((i+1)/2)-1;
	  for(;j>=0;j=((j+1)/2)-1){//updating the key
		  if(key[j]>key[i]){
			  swap(i,j);
			  i=j;
		  }
		  else{
			  break;
		  }
	  }
  }
}
