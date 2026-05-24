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
            int j = i + 1;
            while (j < str.length() && str.charAt(j) != '#') {
                j += 1;
            }
            int length = Integer.parseInt(str.substring(i, j));
            String s = str.substring(j + 1, j + length + 1);
            res.add(s);
            i = j + length + 1;
        }

        return res;
    }
}
