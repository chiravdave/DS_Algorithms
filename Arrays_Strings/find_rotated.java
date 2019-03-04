//Find a no in a rotated array

class Rotated{

     int a[];

     public static void main(String []args){
        Rotated ob = new Rotated();
        ob.a = new int[]{2,3,4,5,1};
        int index = ob.search(3);
        if(index != -1){
            System.out.println("No found at index "+index);
        }
        else{
            System.out.println("No not found");
        }
     }
     
     int search(int check){
         int low=0, high = a.length-1, middle=0;
         while(low<=high){
             middle = (low+high)/2;
             if(a[middle] == check){
                 return middle;
             }
             else if(a[low]<=a[middle]){
                 if(check>= a[low] && check<a[middle]){
                   high = middle - 1;
                 }
                 else{
                     low = middle + 1;
                 }
             }
             else{
                 if(check>a[middle] && check<=a[high]){
                   low = middle + 1;
                    }
                 else{
                    high = middle - 1; 
                 }
             }
         }
         return -1;
     }
}
