class Solution(object):
    def numIslands(self, grid):
        a=set()
        rows1=len(grid)-1
        cols1=len(grid[0])-1
        count=0
        def dfs(rows,cols):
            if (rows,cols) in a:
                return
            if grid[rows][cols]=='1':
                a.add((rows,cols))
            elif grid[rows][cols]=='0':
                return
            if rows>0:
                dfs(rows-1,cols)
            if cols>0:
                dfs(rows,cols-1)
            if rows<rows1:
                dfs(rows+1,cols)
            if cols<cols1:
                dfs(rows,cols+1)
            return
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1' and (i,j) not in a:
                    count+=1
                    dfs(i,j) 
        return count