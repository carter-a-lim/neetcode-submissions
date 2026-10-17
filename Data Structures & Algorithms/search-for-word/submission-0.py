class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = set()

        def next(x,y,curr):
            if x<0 or y<0 or x>len(board[0])-1 or y>len(board)-1 or (x,y) in seen or board[y][x] != word[curr]:
                return False

            curr += 1
            if curr == len(word):
                return True

            seen.add((x,y))

            if not (next(x+1,y,curr) or
                next(x-1,y,curr) or
                next(x,y+1,curr) or
                next(x,y-1,curr)):
               seen.remove((x,y))
            else:
                return True 

        for x in range(len(board[0])):
            for y in range(len(board)):
                if next(x,y,0):
                    return True
        return False

