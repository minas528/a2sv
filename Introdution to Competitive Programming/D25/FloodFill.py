class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image == [] or image == [[]]:
            return image
        
        R= len(image)
        C= len(image[0])
                    
        visited = set()
        visited.add((sr,sc))
        color= image[sr][sc]
        
        def paint(sr,sc):
            image[sr][sc]= newColor
            
            for nr,nc in ((sr+1,sc), (sr-1,sc), (sr,sc+1), (sr,sc-1)):
                if (0 <= nr < R and 0 <=nc < C):
                    if image[nr][nc] == color and (nr,nc) not in visited:
                        visited.add((nr,nc))
                        paint(nr,nc)
        paint(sr,sc)
        
        return image
