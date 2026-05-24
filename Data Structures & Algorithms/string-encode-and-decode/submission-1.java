class Solution {
    int[] arr;

    public String encode(List<String> strs) {
        this.arr = new int[strs.size()];
        int i = 0;
        StringBuilder sb = new StringBuilder();
        for (String s : strs) {
            this.arr[i] = s.length();
            sb.append(s);
            i++;
        }
        return sb.toString();
    }

    public List<String> decode(String str) {
        List<String> res = new ArrayList<>();
        int s = 0;
        for (int n : this.arr) {
            if (n == 0) {
                res.add("");
            } else {
                int end = s + n;
                res.add(str.substring(s, end));
                s = end;
            }
        }
        return res;
    }
}
