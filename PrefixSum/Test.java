package PrefixSum;
import java.util.*;

public class Test{
    public void run(){
        Scanner sc = new Scanner(System.in);

        //변수 입력
        int n = sc.nextInt();
        int m = sc.nextInt();

        int[] inputArr =new int[n];
        for(int i=0;i<n;i++){
            inputArr[i] = sc.nextInt();
        }

        int[][] quest = new int[m][2];
        List<Integer> resultList = new ArrayList<>();

        for(int i=0;i<m;i++){
            quest[i][0] = sc.nextInt()-1;
            quest[i][1] = sc.nextInt()-1;
        }

        //prefix 선언 및 초기화
        int[] prefixArr = new int[n+1];
        prefixArr[0] = 0;
        for(int i=0;i<n;i++){
            prefixArr[i+1] = prefixArr[i] + inputArr[i];
        }

        for(int[] q:quest){
            int start = q[0];
            int end = q[1];

            int result = prefixArr[end+1]-prefixArr[start];
            resultList.add(result);
        }

        for(int result:resultList){
            System.out.println(result);
        }

        sc.close();
    }
}