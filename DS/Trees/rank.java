/* Rank from Stream: Imagine you are reading in a stream of integers. Periodically, you wish
   to be able to look up the rank of a number x (the number of values less than or equal to x).
   Implement the data structures and algorithms to support these operations. That is, implement
   the method track(int x), which is called when each number is generated, and the method
   getRankOfNumber(int x), which returns the number of values less than or equal to x (not including x itself).
   EXAMPLE:
     Stream(in order of appearance):5, 1, 4, 4, 5, 9, 7, 13, 3
     getRankOfNumber(l) 0
     getRankOfNumber(3) 1
     getRankOfNumber(4) 3
*/

import java.util.Scanner;

class Node{

    int val, counter;
    Node left, right;

    Node(int val, int counter){
        this.val = val;
        this.counter = counter;
        left = null;
        right = null;
    }
}

class BST{

    Node root;
    
    void track(int val){
        if(root == null){
         root = new Node(val, 0);   
        }
        else{
            int counter = 0;
            Node temp = root;
            while(true){
             if(val == temp.val){
                 temp.counter++;
                 break;
             }
             else if(val < temp.val){
                 temp.counter++;
                 if(temp.left != null){
                     temp = temp.left;
                 }
                 else{
                     Node n = new Node(val, counter);
                     temp.left = n;
                     break;
                 }
             }
             else{
                 counter = counter + 1 + temp.counter;
                 if(temp.right != null){
                     temp = temp.right;
                 }
                 else{
                     Node n = new Node(val, counter);
                     temp.right = n;
                     break;
                 }
              }
            }
        }
    }
    
    int getRankOfNumber(int val){
        int rank = 0;
        Node temp = root;
        while(temp != null){
            if(temp.val == val){
                return(rank + temp.counter);
            }
            else if(val > temp.val){
                rank = rank + temp.counter;
                temp = temp.right;
            }
            else{
                temp = temp.left;
            }
        }
        return -1;
    }
}

class Rank{
     
     public static void main(String []args){
        BST tree = new BST();
        int ch, n;
        Scanner s = new Scanner(System.in);
        System.out.println("Enter 1 to insert a no;2 for getting rank of a no and 3 to exit");
        while(true){
            System.out.println("Enter your choice");
            ch = s.nextInt();
            switch(ch){
                case 1: System.out.println("Enter a no");
                          n = s.nextInt();
                          tree.track(n);
                          break;
                case 2: System.out.println("Enter the no whose rank you want to find");
                          n = s.nextInt();
                          System.out.println("Rank is:"+tree.getRankOfNumber(n));
                          break;
                case 3: return;
            }
        }
     }
}
