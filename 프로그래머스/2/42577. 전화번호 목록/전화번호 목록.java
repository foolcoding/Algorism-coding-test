import java.util.Arrays;
class Solution {
    public boolean solution(String[] ph) {
        boolean answer = true;
        Arrays.sort(ph);
        for(int i = 0; i < ph.length - 1; i++){
            if(ph[i+1].startsWith(ph[i])){
                 answer = false;
                 break;
            }
        }
        return answer;
    }
}