from __future__ import annotations

class Word():
    """Create a Word in a Free Group. Please pass in a reduced word...
    """
    def __init__(self, x: list[str], x_pow: list[int]) -> None:
        self.letters = x
        self.pows = x_pow

    def __str__(self) -> str:
        s = '\\('
        for i in range(len(self.letters)):
            s += self.letters[i]
            if self.pows[i] != 1:
                s += f'^{{{str(self.pows[i])}}}'
        return s + '\\)'
    
    def __add__(self, w: Word) -> Word:
        i = len(self.letters)-1

        x = self.letters.copy()
        x.extend(w.letters)
        x_pow = self.pows.copy()
        x_pow.extend(w.pows)

        while i < len(x)-1 and x[i] == x[i+1]:
            if x_pow[i] == -x_pow[i+1]:
                x.pop(i)
                x.pop(i)
                x_pow.pop(i)
                x_pow.pop(i)
                i -= 1
            else:
                x_pow[i] += x_pow[i+1]
                x_pow.pop(i+1)
                x.pop(i+1)
        
        return Word(x, x_pow)