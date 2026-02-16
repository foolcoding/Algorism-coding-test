import java.util.*;
class Solution {
    public long solution(int n, int[] time) {
        Arrays.sort(time);
        long low = 1;
        long high = (long) time[time.length - 1] * n;
        long mid = 0;
        long answer = high;
        long sum;
        
        while(low <= high){
            mid = (low + high) / 2;
            sum = 0;
            for(int num : time){
                sum += mid / num;
            }
            if((long)n <= sum){
                answer = mid;
                high = mid - 1;
            }
            else{
                low = mid + 1;
            }
        }
        return answer;
    }
}