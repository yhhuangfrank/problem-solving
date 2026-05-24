class Solution {

    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for (String s : strs) {
            sb.append(s.length());
            sb.append("#");
            sb.append(s);
        }
        return sb.toString();
    }

    public List<String> decode(String str) {
        List<String> res = new ArrayList<>();
        int s = 0;
        while (s < str.length()) {
            char c = str.charAt(s);
            if (c - '0' >= 0 && c - '0' <= 9) {
                int temp = s + 1;
                while (str.charAt(temp) != '#') {
                    temp++;
                }
                int len = Integer.parseInt(str.substring(s, temp));
                res.add(str.substring(temp + 1, temp + len + 1));
                s = temp + len + 1;
            }
        }
        return res;
    }
}
