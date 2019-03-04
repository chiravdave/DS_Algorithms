//Implemented stack with sorting capability; sorting no.s in ascending order from top to bottom

import java.util.Scanner;

class Stack{

    int storage[];
    int top;

    Stack(int size){
        storage = new int[size];
        top = -1;
    }
    
    void push(int val){
        if(top == storage.length){
            System.out.println("Stack is full");
        }
        else{
            storage[++top] = val;
            //System.out.println("Inserted");
        }
    }
    
    int pop(){
        if(top == -1){
            return -1;
        }
        else{
            return storage[top--];
        }
    }

    //Printing the numbers present in the stack
    void showNos(){
        if(top == -1){
            System.out.println("Stack is empty");
        }
        else{
            for(int i=0; i<=top; i++){
                System.out.print(storage[i]+"\t");
            }
            System.out.println();
        }
    }
    
    void sort(){
        //Temporary stack that will hold numbers in the reverse order
        Stack temp = new Stack(storage.length);
        while(top!=-1){
            int val = pop();
            push_temp(val, temp);
        }
        moveAll(temp);
    }
    
    private void push_temp(int val, Stack temp){
        //Pop numbers from the temporary stack until it finds it's correct position
        while(temp.top != -1 && temp.storage[temp.top]>val){
            int remove = temp.pop();
            push(remove);
        }
        temp.push(val);
    }
    
    private void moveAll(Stack temp){
        while(temp.top != -1){
            push(temp.pop());
        }
    }
}

class Main{

     public static void main(String []args){
        Scanner s = new Scanner(System.in);
        int ch, val;
        System.out.println("Enter size of the stack");
        int size = s.nextInt();
        Stack stack = new Stack(size);
        System.out.println("Enter 1 to push\nEnter 2 to pop\nEnter 3 to show\nEnter 4 to sort\nEnter 5 to exit");
        while(true){
            System.out.println("Enter your choice");
            ch = s.nextInt();
            switch(ch){
                case 1: System.out.println("Enter the element");
                        val = s.nextInt();
                        stack.push(val);
                        break;
                        
                case 2: val = stack.pop();
                        if(val == -1){
                          System.out.println("Stack no."+stack+" is empty");
                        }
                        else{
                          System.out.println("Element popped out is="+val);   
                        }
                        break;
                        
                case 3: stack.showNos();
                        break;
                        
                case 4: stack.sort();
                        break;
                        
                case 5: return;
            }
        }
     }
}