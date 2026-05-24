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
                pairs.set(insertIndex + 1, pairs.get(insertIndex));
                insertIndex--;
            }
            if (insertIndex + 1 != i) {
                pairs.set(insertIndex + 1, insertValue);
            }
            addNewList(pairs, res);
        }
        return res;
    }

    public void addNewList(List<Pair> pairs, List<List<Pair>> res) {
        List<Pair> list = new ArrayList<>();
        for (Pair p : pairs) {
            list.add(p);
        }
        res.add(list);
    }
}
