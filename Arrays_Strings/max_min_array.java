//Find max and min in a given array in log(n) time

class MaxMin {

  int a[];
  
  public static void main(String[] args) {
    MaxMin ob = new MaxMin();
    ob.a = new int[]{8,3,1,5,10};
    int res[]= ob.maxMin(0, ob.a.length-1);
    System.out.println("Min is:"+res[0]+"\n"+"Max is:"+res[1]);
   }
 
  //This methods finds the max and min inside the array
  private int[] maxMin(int low, int high)
  {
   if(low == high){
      return new int[]{a[low], a[low]};
   }
   else{
	int mid=(low+high)/2;   // divide the set into two equal sized subsets and solve them simultaneously  
	int left_min_max[] = maxMin(low, mid);  
	int right_min_max[] = maxMin(mid+1, high);
	int min_max[]=new int[2];
	min_max[0] = Math.min(left_min_max[0], right_min_max[0]);
	min_max[1] = Math.max(left_min_max[1], right_min_max[1]);
	return min_max;
	}
     }
}
