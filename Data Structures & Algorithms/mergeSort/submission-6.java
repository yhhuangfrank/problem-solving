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
        return mergeSortHelper(pairs, 0, pairs.size() - 1);
    }

    public List<Pair> mergeSortHelper(List<Pair> lst, int s, int e) {
        if (e - s + 1 <= 1) return lst;
        int m = s + (e - s) / 2;
        mergeSortHelper(lst, s, m);
        mergeSortHelper(lst, m + 1, e);
        merge(lst, s, m, e);
        return lst;
    }

    public void merge(List<Pair> lst, int s, int m, int e) {
        List<Pair> l = new ArrayList<>(lst.subList(s, m + 1));
        List<Pair> r = new ArrayList<>(lst.subList(m + 1, e + 1));

        int i = 0;
        int j = 0;
        int k = s;

        while (i < l.size() && j < r.size()) {
            if (l.get(i).key <= r.get(j).key) {
                lst.set(k, l.get(i));
                i += 1;
            } else {
                lst.set(k, r.get(j));
                j += 1;
            }
            k += 1;
        }

        while (i < l.size()) {
            lst.set(k, l.get(i));
            i += 1;
            k += 1;
        }
        while (j < r.size()) {
            lst.set(k, r.get(j));
            j += 1;
            k += 1;
        }
    }
}
