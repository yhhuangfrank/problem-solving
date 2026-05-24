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
        List<Pair> l = new ArrayList<>();
        List<Pair> r = new ArrayList<>();
        for (int i = 0; i <= mid; i++) {
            l.add(pairs.get(i));
        }
        for (int i = mid + 1; i < pairs.size(); i++) {
            r.add(pairs.get(i));
        }

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
            for (int i = l; i < left.size(); i++) {
                res.add(left.get(i));
            }
        } else {
            for (int i = r; i < right.size(); i++) {
                res.add(right.get(i));
            }
        }
        return res;
    }
}
