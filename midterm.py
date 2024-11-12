from __future__ import annotations
from Permutations import Permutation

class SymmetricCyclicSubgroup:
    def __init__(self, p: Permutation) -> None:
        self.l = []
        self.n = p.n
        p_tmp = Permutation(p.d, p.n)
        self.l.append(p_tmp)
        while not p_tmp == Permutation({},p.n):
            p_tmp *= p
            self.l.append(p_tmp)
    
    def intersection(self, gp: SymmetricCyclicSubgroup, prnt: bool = False) -> None:
        l = []
        for p in self.l:
            for q in gp.l:
                if p == q and not p in l:
                    l.append(p)
        if len(l) == self.n:
            if prnt:
                print(f'<{self.l[0]}> = <{gp.l[0]}>')
        else:
            if prnt:
                print(f'<{self.l[0]}> && <{gp.l[0]}> = {l}')
            if not len(l) == 1:
                return False
        return True

def gen_n_cycles(n: int) -> list[SymmetricCyclicSubgroup]:
    l = ['(1']
    for _ in range(2,n+1):
        new_l = []
        for s in l:
            for i in range(2,n+1):
                if s.count(f'{i}') == 0:
                    new_l.append(s+f' {i}')
        l = new_l
    for i in range(len(l)):
        l[i] += ')'
    return l

def test_intersections(n: int):
    l = gen_n_cycles(n)
    for i in range(len(l)):
        l[i] = SymmetricCyclicSubgroup(Permutation(l[i], n))
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if not l[i].intersection(l[j]):
                l[i].intersection(l[j], True)
                return

test_intersections(9)