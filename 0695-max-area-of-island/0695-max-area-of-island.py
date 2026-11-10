class Solution(object):
    def maxAreaOfIsland(self, grid):
        visited=set()
        rows=len(grid)
        col=len(grid[0])
        maxi=0
        def bfs(i,j):
            q=deque()
            q.append((i,j))
            visited.add((i,j))
            count=0
            while q:
                a,b=q.popleft()
                count+=1
                direction=[(0,1),(1,0),(0,-1),(-1,0)]
                for di,dj in direction:
                    ni,nj=a+di,b+dj
                    if (0<=ni<rows and 0<=nj<col and grid[ni][nj]==1 and (ni,nj) not in visited):
                        q.append((ni,nj))
                        visited.add((ni,nj))
            return count
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1 and (i,j) not in visited:
                    maxi=max(maxi,bfs(i,j))
        return maxi
            
        