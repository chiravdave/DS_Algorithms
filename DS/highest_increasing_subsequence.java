//Program to find highest increasing subsequence in a given array

class HIS {

	private int a[];

	public static void main(String[] args) {
		HIS ob = new HIS();
                ob.a=new int[]{8,3,9,4,10};
		ob.calculate();
	}

	private void calculate()
	{
		int n=a.length;
		int max=1;
		int l[]=new int[n]; //to store length of increasing subsequence 
		int p[]=new int[n]; //to store the increasing subsequence
		for(int i=0;i<n;i++){
			l[i]=1;  //by default a single character is a sequence of unit length
			p[i]=i;  
		}
		for(int i=1;i<n;i++){
			for(int j=0;j<i;j++){ // finding previous highest subsequence
			if(a[i]>a[j]){
				if(l[j]+1>l[i]){  //checking if this is a higher length subsequence
					l[i]=l[j]+1;
					p[i]=j;
					max=Math.max(max,l[i]);
				}
			}
		}
	 }
		//print all such possible subsequence
		for(int i=0;i<n;i++){
			if(l[i]==max){
				System.out.print("Length:"+max+"\t");
				printSequence(p,i);
				System.out.println();
			}
		}
	}

	private void printSequence(int p[],int h){
		if(p[h]==h)
			System.out.print(a[h]);
		else{
			printSequence(p,p[h]);
			System.out.print("-->"+a[h]);
	}
  }
}
