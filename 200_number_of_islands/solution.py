class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.gridWidth = len(grid)
        self.gridHeight = len(grid[0])

        self.islandCount = 0

        #binary grid to track which grids have been scanned
        #0 means not scanned, 1 means scanned 
        self.scannedGrids = []
        row = []
        for i in range(self.gridWidth):
            for j in range(self.gridHeight):
                row.append(0)
            self.scannedGrids.append(row)
            row = []

        def searchAbove(self, coords):
            i = coords[0]
            j = coords[1]
            if self.isScannedAlready(i, j):
                return None
            if i == 0 or grid[i-1][j] == 0:
                return None
            return [i, j]

        def searchLeft(self, coords):
            i = coords[0]
            j = coords[1]
            if self.isScannedAlready(i, j):
                return None
            if j == self.gridWidth-1 or grid[i][j+1] == 0:
                return None
            return [i, j]

        def searchBelow(self, coords):
            i = coords[0]
            j = coords[1]
            if self.isScannedAlready(i, j):
                return None
            if i == self.gridHeight-1 or grid[i+1][j] == 0:
                return None
            return [i, j]

        def searchRight(self, coords):
            i = coords[0]
            j = coords[1]
            if self.isScannedAlready(i, j):
                return None
            if j == 0 or grid[i][j-1] == 0:
                return None
            return [i, j]

        def isScannedAlready(self, coords):
            i = coords[0]
            j = coords[1]
            if self.scannedGrids[i,j] == 1:
                return True
            return False
        
        #searches for land above, left, below, and right of the given coordinate
        #returns a 4 element long list, with 1 meaning land, 0 meaning sea
        #[above, left, below, right]
        def searchForAdjacentLand(self, coords):
            i = coords[0]
            j = coords[1]
            landScan = []
            landScan.append(self.searchAbove(i,j))
            landScan.append(self.searchLeft(i,j))
            landScan.append(self.searchBelow(i,j))
            landScan.append(self.searchRight(i,j))
            for coords in landScan:
                if coords != None:
                    searchForAdjacentLand(self, coords)
            else:
                #increment island count 
                self.islandCount += 1

        #loops through scannedGrids to find a 0
        #if 0 is found, return coordinates
        #if 0 is not found (scannedGrids is all 1s), return empty array
        def searchForNewIsland(self):
            #search for 0 in scannedGrids
            for i in range(self.gridWidth):
                for j in range(self.gridHeight):
                    isGridScanned = self.scannedGrids[i][j]
                    self.scannedGrids[i][j] = 1
                    if isGridScanned == 0 and grid[i][j] == 1:
                        return [i, j]
            #no zeros are found, return []
            return None

        newIslandCoords = searchForNewIsland(self)
        while newIslandCoords != None:
            searchForAdjacentLand(self, newIslandCoords)
            newIslandCoords = searchForNewIsland(self)

        return self.islandCount
