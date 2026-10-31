class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
    
        def buildSeq(rowConditions):
            prerequsites = defaultdict(list)

            for pre, cur in rowConditions:
                prerequsites[cur].append(pre)
            
            res = []
            visit = set()
            path = set()

            def dfs(i):
                if i in path:
                    return False # Cycle
                if i in visit:
                    return True
                visit.add(i)
                path.add(i)
                for pre in prerequsites[i]:
                    if not dfs(pre):
                        return False
                path.remove(i)
                res.append(i)

                return True

            for i in range(1, k + 1):
                if not dfs(i):
                    return []
            return res
        
        rowSeq = buildSeq(rowConditions)
        colSeq = buildSeq(colConditions)
        # print(f'rowSeq: {rowSeq}, colSeq: {colSeq}')
        if not rowSeq or not colSeq:
            return []
        matrix = [[0] * k for _ in range(k)]
        pos = {i: [0, 0] for i in range(1, k + 1)} # i: [r, c]
        for i, r in enumerate(rowSeq):
            pos[r][0] = i
        for i, c in enumerate(colSeq):
            pos[c][1] = i
        for i, (r, c) in pos.items():
            matrix[r][c] = i
        return matrix
                
