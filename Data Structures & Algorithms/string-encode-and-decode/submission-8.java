class Solution {

    public String encode(List<String> strs) {
        StringBuilder res = new StringBuilder();
        for (String s : strs) {
            res.append(s.length());
            res.append("#");
            res.append(s);
        }
        return res.toString();
    }

    public List<String> decode(String str) {
        List<String> res = new ArrayList<>();
        int i = 0;
        while (i < str.length()) {
            char c = str.charAt(i);
            if (c >= '0' && c <= '9') {
                int j = i + 1;
                while (str.charAt(j) != '#') {
                    j++;
                }
                int len = Integer.parseInt(str.substring(i, j));
                String s = str.substring(j + 1, j + 1 + len);
                res.add(s);
                i = j + 1 + len;
            } else {
                i++;
            }
        }
        return res;
    }
}
