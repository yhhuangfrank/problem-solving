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
        if (pairs.isEmpty()) return pairs;
        return mergeSortHelper(pairs, 0, pairs.size() - 1);
    }

    public List<Pair> mergeSortHelper(List<Pair> pairs, int left, int right) {
        if (pairs.size() == 1) return pairs; // one element

        int mid = left + (right - left) / 2;
        List<Pair> l = pairs.subList(0, mid + 1);
        List<Pair> r = pairs.subList(mid + 1, pairs.size());
        return merge(mergeSortHelper(l, 0, l.size() - 1), mergeSortHelper(r, 0, r.size() - 1));
    }

    public List<Pair> merge(List<Pair> left, List<Pair> right) {
        List<Pair> res = new ArrayList<>();
        int l = 0;
        int r = 0;

        while (l < left.size() && r < right.size()) {
            if (left.get(l).key <= right.get(r).key) {
                res.add(left.get(l));
                l++;
            } else {
                res.add(right.get(r));
                r++;
            }
        }

        if (l < left.size()) {
            res.addAll(left.subList(l, left.size()));
        } else {
            res.addAll(right.subList(r, right.size()));
        }
        return res;
    }
}
