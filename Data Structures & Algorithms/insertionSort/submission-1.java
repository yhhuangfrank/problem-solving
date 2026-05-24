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
        if (pairs.isEmpty()) return res;

        addNewList(pairs, res);
        for (int i = 1; i < pairs.size(); i++) {
            int insertIndex = i - 1;
            Pair insertValue = pairs.get(i);
            int key = insertValue.key;
            while (insertIndex >= 0 && pairs.get(insertIndex).key > key) {
                swap(pairs, insertIndex, insertIndex + 1);
                insertIndex--;
            }
            addNewList(pairs, res);
        }
        return res;
    }

    public void swap(List<Pair> pairs, int i, int j) {
        Pair temp = pairs.get(i);
        pairs.set(i, pairs.get(j));
        pairs.set(j, temp);
    }

    public void addNewList(List<Pair> pairs, List<List<Pair>> res) {
        List<Pair> list = new ArrayList<>();
        for (Pair p : pairs) {
            list.add(p);
        }
        res.add(list);
    }
}
