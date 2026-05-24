// Definition for a pair
// class Pair {
//     int key;
//     String value;
//
//     Pair(int key, String value) {
//         this.key = key;
//         this.value = value;
//     }
// }
public class Solution {
    public List<List<Pair>> insertionSort(List<Pair> pairs) {
        List<List<Pair>> res = new ArrayList<>();

        for (int i = 0; i < pairs.size(); i++) {
            int j = i - 1;
            while (j >= 0 && pairs.get(j + 1).key < pairs.get(j).key) {
                swap(j, j + 1, pairs);
                j -= 1;
            }
            List<Pair> clone = new ArrayList<>(pairs);
            res.add(clone);
        }
        return res;
    }

    public void swap(int x, int y, List<Pair> list) {
        Pair temp = list.get(x);
        list.set(x, list.get(y));
        list.set(y, temp);
    }
}
