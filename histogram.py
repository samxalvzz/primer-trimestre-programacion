"""
histogram([1, 3, 4], "#") -> "#\n###\n####"
histogram([3, 5, 1, 8], "¬") -> '¬¬¬\n¬¬¬¬¬\n¬\n¬¬¬¬¬¬¬¬'
"""

def histogram(lst: list[int], char: str) -> str:
    res = []
    i = 0
    while i < len(lst):
        res.append(char * lst[i])
        i += 1
    return "\n".join(res)