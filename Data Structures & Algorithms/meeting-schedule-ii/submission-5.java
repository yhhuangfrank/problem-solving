/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

class Solution {
    public int minMeetingRooms(List<Interval> intervals) {
        Map<Integer, Integer> map = new HashMap<>(); // {time: count}
        List<Integer> timeList = new ArrayList<>();
        for (Interval i : intervals) {
            if (!map.containsKey(i.start)) {
                map.put(i.start, 0);
                timeList.add(i.start);
            }
            if (!map.containsKey(i.end)) {
                map.put(i.end, 0);
                timeList.add(i.end);
            }
            map.put(i.start, map.get(i.start) + 1);
            map.put(i.end, map.get(i.end) - 1);
        }
        timeList.sort((a, b) -> a - b);
        int maxOverlap = 0;
        int prefixSum = 0;
        for (int time : timeList) {
            prefixSum += map.get(time);
            maxOverlap = Math.max(maxOverlap, prefixSum);
        }
        return maxOverlap;
    }
}
