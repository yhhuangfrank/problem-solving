class Solution {
    private Map<Character, Set<Character>> adj = new HashMap<>();
    private Set<Character> visit = new HashSet<>();
    private Set<Character> path = new HashSet<>();
    private List<Character> resultArr = new ArrayList<>();

    public String foreignDictionary(String[] words) {
        
        for (String w : words) {
            for (int i = 0; i < w.length(); i++) {
                char c = w.charAt(i);
                adj.putIfAbsent(c, new HashSet<>());
            }
        }
        
        for (int i = 0; i < words.length - 1; i++) {
            String w1 = words[i];
            String w2 = words[i + 1];
            int minLen = Math.min(w1.length(), w2.length());
            boolean isPrefix = w1.substring(0, minLen).equals(w2.substring(0, minLen));
            
            if (w1.length() > w2.length() && isPrefix) return "";

            for (int j = 0; j < minLen; j++) {
                char c1 = w1.charAt(j);
                char c2 = w2.charAt(j);
                if (c1 != c2) {
                    adj.get(c1).add(c2);
                    break;
                }
            }
        }
        
        for (Character c : adj.keySet()) {
            if (!dfs(c)) return "";
        }

        StringBuilder res = new StringBuilder();
        for (int i = resultArr.size() - 1; i >= 0; i--) {
            res.append(resultArr.get(i));
        }
        return res.toString();
    }

    private boolean dfs(Character c) {
        if (path.contains(c)) {
            return false;
        }
        if (visit.contains(c)) {
            return true;
        }
        visit.add(c);
        path.add(c);
        for (Character neigh : adj.get(c)) {
            if (!dfs(neigh)) return false;
        }
        path.remove(c);
        resultArr.add(c);
        return true;
    }
}
