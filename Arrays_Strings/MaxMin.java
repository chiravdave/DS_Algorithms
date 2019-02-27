//Find max and min in a given array in log(n) time
public class MaxMin {
	public static void main(String[] args) {
		int a[]=new int[]{8,3,1,5,10};
		int res[]=maxmin(a,0,a.length-1);
		System.out.println("Min is:"+res[0]+"\n"+"Max is:"+res[1]);
	}
	private static int[] maxmin(int a[],int l,int h)
	{
		if(l==h-1)
			if (a[l]>a[h])
			   return new int[]{a[h],a[l]};
			else
			   return new int[]{a[l],a[h]};
		else{
			 int mid=(l+h)/2;         // divide the set into two equal sized subsets and solve them simultaneously  
			 int a1[]=maxmin(a,0,mid);  
			 int a2[]=maxmin(a,mid,h);
			 int mm[]=new int[2];
			 mm[0]=Math.min(a1[0],a2[0]);
			 mm[1]=Math.max(a1[1],a2[1]);
			 return mm;
		}
	}
}
