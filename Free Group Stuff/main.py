from __future__ import annotations
from random import randint, choice
from itertools import combinations_with_replacement, permutations

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
    
    def __pow__(self, n: int) -> Word:
        w = Word(self.letters, self.pows)
        if n < 0:
            w.letters = list(reversed(w.letters))
            w.pows = [-1*i for i in reversed(w.pows)]
        new_w = Word(w.letters, w.pows)
        for _ in range(abs(n)-1):
            new_w += w
        return new_w

class Commutator:
    def __init__(self, w1: Word, w2: Word) -> None:
        self.w1 = w1
        self.w2 = w2
        self.w = w1**-1+w2**-1+w1+w2

    def __str__(self) -> str:
        return f'[{str(self.w1)}, {str(self.w2)}]'
    
    def full_string(self) -> str:
        return str(self.w)
    
    def max_exp(self, ltr: str) -> int:
        m = 0
        for i in range(len(self.w.letters)):
            if self.w.letters[i] == ltr and abs(self.w.pows[i]) > m:
                m = abs(self.w.pows[i])
        return m
    
    def __add__(self, c: Commutator) -> Commutator:
        new_c = Commutator(self.w1, self.w2)
        new_c.w = self.w
        new_c.w += c.w
        return new_c
    
def random_word(letters: list[str], pow_bound: int = 20, len_bound: int = 20) -> Word:
    l = randint(1, len_bound)
    w = Word([choice(letters)], [choice([-1,1])*randint(1,pow_bound)])
    for _ in range(l-1):
        w += Word([choice(letters)], [choice([-1,1])*randint(1,pow_bound)])
    return w

def random_commutator(letters: list[str], pow_bound: int = 20, len_bound: int = 20) -> Commutator:
    w1 = random_word(letters, pow_bound, len_bound)
    w2 = random_word(letters, pow_bound, len_bound)
    while len(w1.letters) == 0:
        w1 = random_word(letters, pow_bound, len_bound)
    while len(w2.letters) == 0:
        w2 = random_word(letters, pow_bound, len_bound)
    return Commutator(w1, w2)

def find_max_combo(l: list[Commutator], x: int) -> int:
    c = list(combinations_with_replacement(l, x))
    m = 0
    for comb in c:
        for combo in permutations(comb):
            tmp = None
            for t in combo:
                if tmp == None:
                    tmp = t
                else:
                    tmp += t
            if tmp.max_exp('a') > m:
                # for o in combo:
                #     print(o)
                # print(tmp.full_string())
                m = tmp.max_exp('a')
    return m

def interesting_search():
    cnt = 1
    while True:
        print(cnt)
        cnt += 1
        l = [random_commutator(['a','b'],5,10) for _ in range(4)]
        l2 = find_max_combo(l, 2)
        l3 = find_max_combo(l, 3)
        l4 = find_max_combo(l, 4)
        if l2 < l3 and l3 < l4:
            for c in l:
                print(c.full_string())
                return

interesting_search()