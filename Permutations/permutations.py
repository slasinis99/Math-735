from __future__ import annotations

class Permutation:
    def __init__(self, d: dict|str, n) -> None:
        self.n = n
        self.d = {}
        if isinstance(d, dict):
            for i in range(1,n+1,1):
                if not d.get(i) is None:
                    self.d[i] = d[i]
                else:
                    self.d[i] = i
        elif isinstance(d, str):
            m = -1
            for s in d.split('('):
                if s == '':
                    continue
                s = s[0:len(s)-1].split(' ')
                for i, v in enumerate(s):
                    self.d[int(v)] = int(s[(i+1) % len(s)])
        domain = set(self.d.keys())
        codomain = set(self.d.values())
        if not domain == codomain or not len(domain) == len(codomain):
            raise ValueError()

    def __str__(self) -> str:
        s = '(1'
        cycle_start = 1
        cycle_recent = 1
        cycle_seen = [1]
        while True:
            nxt = self[cycle_recent]
            if nxt == cycle_start:
                cycle_recent = min([i if not i in cycle_seen else self.n+1 for i in range(1,self.n+1)])
                cycle_seen.append(cycle_recent)
                cycle_start = cycle_recent
                if cycle_recent == self.n+1:
                    s += ')'
                    if s[0:3] == '(1)':
                        if s == '(1)':
                            return '1'
                        else:
                            return s[3:len(s)]
                    return s
                if self[cycle_recent] == cycle_recent:
                    continue
                s += f')({cycle_recent}'
                continue
            s += f' {nxt}'
            cycle_recent = nxt
            cycle_seen.append(cycle_recent)
    
    def __getitem__(self, i: int) -> int:
        if not self.d.get(i) is None:
            return self.d[i]
        else:
            return i

    def __repr__(self) -> str:
        return str(self)
    
    def __mul__(self, y: Permutation) -> Permutation:
        new_d = {}
        for i in range(1, max(self.n, y.n)+1):
            new_d[i] = self[y[i]]
        return Permutation(new_d, max(self.n, y.n))
    
    def __pow__(self, x: int) -> Permutation:
        if x == 0:
            return Permutation({}, self.n)
        if x < 0:
            new_p = Permutation({v:k for k, v in self.d.items()}, self.n)
            return new_p**abs(x)
        p = self
        for _ in range(x-1):
            p = p*self
        return p
    
    def __eq__(self, o: Permutation) -> bool:
        return self.d == o.d