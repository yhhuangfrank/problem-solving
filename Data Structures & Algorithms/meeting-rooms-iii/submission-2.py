class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        unused_rooms = [i for i in range(n)]
        using_rooms = [] # (end time of a room, index)
        meetings.sort(key=lambda m: m[0])
        usedCount = {i: 0 for i in range(n)}

        for s, e in meetings:
            while using_rooms and using_rooms[0][0] <= s:
                end_time, id = heapq.heappop(using_rooms)
                heapq.heappush(unused_rooms, id)
            room_id = None
            next_end_time = None
            if unused_rooms:
                room_id = heapq.heappop(unused_rooms)
                next_end_time = e
            else:
                end_time, id = heapq.heappop(using_rooms)
                room_id = id
                next_end_time = end_time + (e - s)
            usedCount[room_id] += 1
            heapq.heappush(using_rooms, (next_end_time, room_id))

        # print(usedCount)
        result = [(-c, i) for i, c in usedCount.items()]
        heapq.heapify(result)
        return heapq.heappop(result)[1]