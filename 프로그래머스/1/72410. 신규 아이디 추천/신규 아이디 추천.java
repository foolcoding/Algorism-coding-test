class Solution {
    public String solution(String new_id) {
String answer = "";
		// 1
	new_id = new_id.toLowerCase();
        
        // 2
	for(int i = 0; i < new_id.length(); i++) {
		char ch = new_id.charAt(i);
		if('a' <= ch && ch <= 'z') {
			answer += ch;
		}
		if('0' <= ch && ch <= '9') {
			answer += ch;
		}
		if(ch == '-' || ch == '_' || ch == '.') {
			answer += ch;
		}
	}
	
        // 3
	while(answer.contains("..")) {
		answer = answer.replace("..", ".");
	}
	
        // 4
	if(answer.startsWith(".")) {
		answer = answer.substring(1);	// 1번째 인덱스부터 끝까지 잘라서 다시 대입한다
	}
	if(answer.endsWith(".")) {
		answer = answer.substring(0, answer.length() - 1);	// 0부터 마지막까지(미포함) 잘라서 대입한다
	}

        // 5
	if(answer.equals("")) {
		answer = "a";
	}

    // 6
	if(answer.length() >= 16) {
		answer = answer.substring(0, 15);
		
//	만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
		if(answer.endsWith(".")) {
			answer = answer.substring(0, 14);
		}
	}
        // 7
	while(answer.length() <= 2) {
		answer += answer.substring(answer.length() - 1);
	}

		return answer;
	}
}