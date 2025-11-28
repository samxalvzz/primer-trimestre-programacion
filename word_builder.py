"""
word_builder = (["g", "e", "o"], [1, 0, 2]) -> "ego"
word_builder = (["e", "t", "s", "t"], [3, 0, 2, 1])
"""

def word_builder(ltr: list[str], pos: list[int]) -> str:
    res = []
    
    i = 0
    while i < len(pos):
        res.append(ltr[pos[i]])    
        i += 1
    return "".join(res)