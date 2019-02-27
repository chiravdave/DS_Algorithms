import java.util.Scanner;

class MultiStack{
    int storage[];
    int tops[];
    int n_stacks;
    MultiStack(int n){
        storage = new int[n*3];
        tops = new int[n];
        n_stacks = n;
        /*Stack locations are arranged in consecutive order.i.e for n=3, indexes 0,3,6... for stack-1; 1,4,7.. for stack-2;
          2,5,8.. for stack-3 */
        for(int i=0; i<n; i++){
            tops[i] = i - n_stacks;
        }
    }
    
    void push(int which_one, int val){
        if((tops[which_one-1]+n_stacks) >= storage.length){
            System.out.println("Stack no."+which_one+" is full");
        }
        else{
            tops[which_one-1] = tops[which_one-1] + n_stacks;
            storage[tops[which_one-1]] = val;
            System.out.println("Inserted");
        }
    }
    
    int pop(int which_one){
        if(tops[which_one-1] < (which_one-1)){
            return -1;
        }
        else{
            int val = storage[which_one-1];
            tops[which_one-1] = tops[which_one-1] - n_stacks;
            return val;
        }
    }
    //Print numbers present in the particular stack
    void showNos(int which_one){
        if(tops[which_one-1] < which_one){
            System.out.println("Stack no."+which_one+" is empty");
        }
        else{
            for(int i=which_one-1; i<=tops[which_one-1]; i=i+n_stacks){
                System.out.print(storage[i]+"\t");
            }
            System.out.println();
        }
    }
}

public class HelloWorld{
     public static void main(String []args){
        Scanner s = new Scanner(System.in);
        int ch, stack, val;
        System.out.println("Enter no of stacks");
        int n_stacks = s.nextInt();
        MultiStack stacks = new MultiStack(n_stacks);
        System.out.println("Enter 1 to push\nEnter 2 to pop\nEnter 3 to show\nEnter 4 to exit");
        while(true){
            System.out.println("Enter your choice");
            ch = s.nextInt();
            switch(ch){
                case 1: System.out.println("Enter the element and stack no");
                        val = s.nextInt();
                        stack = s.nextInt();
                        stacks.push(stack, val);
                        break;
                        
                case 2: System.out.println("Enter the stack");
                        stack = s.nextInt();
                        val = stacks.pop(stack);
                        if(val == -1){
                          System.out.println("Stack no."+stack+" is empty");
                        }
                        else{
                          System.out.println("Element popped out is="+val);   
                        }
                        break;
                        
                case 3: System.out.println("Enter the stack");
                        stack = s.nextInt();
                        stacks.showNos(stack);
                        break;
                        
                case 4: return;
            }
        }
     }
}
