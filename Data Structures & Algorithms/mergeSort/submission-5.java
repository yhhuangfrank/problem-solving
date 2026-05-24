// Definition for a pair.
// class Pair {
//     public int key;
//     public String value;
//
//     public Pair(int key, String value) {
//         this.key = key;
//         this.value = value;
//     }
// }
class Solution {
    public List<Pair> mergeSort(List<Pair> pairs) {
        return helper(0, pairs.size(), pairs);
    }

    public List<Pair> helper(int s, int e, List<Pair> list) {
        if (list.size() <= 1) return list;
        int m = s + (e - s) / 2;
        List<Pair> left = list.subList(0, m + 1);
        List<Pair> right = list.subList(m + 1, list.size());
        return merge(helper(0, left.size() - 1, left), helper(0, right.size() - 1, right));
    }

    public List<Pair> merge(List<Pair> left, List<Pair> right) {
        int l = 0;
        int r = 0;
        List<Pair> merged = new ArrayList<>();

        while (l < left.size() && r < right.size()) {
            Pair p1 = left.get(l);
            Pair p2 = right.get(r);

            if (p1.key <= p2.key) {
                merged.add(left.get(l));
                l += 1;
            } else {
                merged.add(right.get(r));
                r += 1;
            }
        }

        while (l < left.size()) {
            merged.add(left.get(l));
            l += 1;
        }

        while (r < right.size()) {
            merged.add(right.get(r));
            r += 1;
        }

        return merged;
    }
}
