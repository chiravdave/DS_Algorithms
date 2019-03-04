// Check if the second string is a roation of the first string

import java.util.Scanner;

class CheckRotation{

     public static void main(String []args){
        Scanner s = new Scanner(System.in);
        System.out.println("Enter 2 strings to check");
        String s1 = s.nextLine();
        String s2 = s.nextLine();
        if(s1.length() != s2.length()){
            System.out.println("The second string is not a rotation of the first");
        }
        else{
            s1 = s1+s1;
            if(s1.indexOf(s2) < 0){
                System.out.println("The second string is not a rotation of the first");
            }
            else{
                 System.out.println("The second string is a rotation of the first");
            }
        }
     }
}
