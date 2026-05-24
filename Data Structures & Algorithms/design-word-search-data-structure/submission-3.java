class WordDictionary {
    private TrieNode root;

    public WordDictionary() {
        this.root = new TrieNode();
    }

    public void addWord(String word) {
        TrieNode cur = this.root;
        for (char c : word.toCharArray()) {
            cur.children.putIfAbsent(c, new TrieNode());
            cur = cur.children.get(c);
        }
        cur.isWord = true;
    }

    public boolean search(String word) {
        return helper(0, this.root, word);
    }

    private boolean helper(int i, TrieNode node, String word) {
        for (int j = i; j < word.length(); j++) {
            char c = word.charAt(j);
            if (c == '.') {
                for (TrieNode neighbor : node.children.values()) {
                    if (helper(j + 1, neighbor, word)) return true;
                }
                return false;
            } else  {
                if (!node.children.containsKey(c)) return false;
                return helper(j + 1, node.children.get(c), word);
            }
        }
        return node.isWord;
    }
}

class TrieNode {
    Map<Character, TrieNode> children;
    boolean isWord;

    public TrieNode() {
        this.children = new HashMap<>();
        this.isWord = false;
    }
}
