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
    public boolean canAttendMeetings(List<Interval> intervals) {
        if (intervals.size() < 2) return true;

        List<Interval> sortedIntervals = intervals.stream()
            .sorted((a, b) -> a.start - b.start)
            .toList();

        for (int i = 1; i < sortedIntervals.size(); i++) {
            Interval prev = sortedIntervals.get(i - 1);
            Interval cur = sortedIntervals.get(i);
            if (cur.start < prev.end) return false;
        }

        return true;
    }
}
