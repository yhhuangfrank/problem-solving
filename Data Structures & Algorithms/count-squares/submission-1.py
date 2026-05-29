class CountSquares:

    def __init__(self):
        self.mapping = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.mapping[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        x1, y1 = point
        # find all possible vertices on the diaganol axis
        for (x2, y2) in self.mapping.keys():
            if abs(x1 - x2) == abs(y1 - y2) and x1 != x2:
                # other verices on the squares
                point1 = (x1, y2)
                point2 = (x2, y1)
                if point1 in self.mapping and point2 in self.mapping:
                    res += (
                        self.mapping[(x2, y2)] * self.mapping[point1] * self.mapping[point2]
                    )
        return res
