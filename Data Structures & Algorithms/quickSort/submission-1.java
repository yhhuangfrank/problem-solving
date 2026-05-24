// Definition for a pair.
// class Pair {
//     int key;
//     String value;
//
//     public Pair(int key, String value) {
//         this.key = key;
//         this.value = value;
//     }
// }
class Solution {
    public List<Pair> quickSort(List<Pair> pairs) {
        if (pairs.isEmpty()) return pairs;
        quickSortHelper(pairs, 0, pairs.size() - 1);
        return pairs;
    }

    private void quickSortHelper(List<Pair> pairs, int low, int high) {
        if (low >= high)
            return;
        int index = partition(pairs, low, high);
        swap(pairs, index, high);
        quickSortHelper(pairs, low, index - 1);
        quickSortHelper(pairs, index + 1, high);
    }

    private int partition(List<Pair> pairs, int low, int high) {
        int pivot = pairs.get(high).key;
        int l = low;
        for (int i = low; i < high; i++) {
            if (pairs.get(i).key < pivot) {
                swap(pairs, i, l);
                l++;
            }
        }
        return l;
    }

    private void swap(List<Pair> pairs, int i , int j) {
        Pair temp = pairs.get(i);
        pairs.set(i, pairs.get(j));
        pairs.set(j, temp);
    }
}   
