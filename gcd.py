def gcd(a, b):
    d = {}
    v = __gcd(a, b, d)
    while not d[v][1] == a and not d[v][3] == b:
        tmp = d[d[v][3]]
        d[v] = [d[v][2], tmp[1], d[v][0]+d[v][2]*tmp[2], d[v][1]]
    print(f'gcd({a}, {b}) = {v} = ({d[v][0]})({d[v][1]}) + ({d[v][2]})({d[v][3]})')

def __gcd(a, b, d = {}):
    if b > a: a, b = b, a
    q = a // b
    r = a % b
    d[r] = [1, a, -q, b]
    if r == 0:
        return b
    return __gcd(b, r, d)

gcd(207885, 60808)