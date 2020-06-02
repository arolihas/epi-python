import collections

Point = collections.namedtuple('x', 'y')

def is_rectangle(a, b, c, d):
    d1 = (a.x - b.x)**2 + (a.y - b.y)**2
    d2 = (a.x - c.x)**2 + (a.y - c.y)**2
    d3 = (a.x - d.x)**2 + (a.y - d.y)**2
    ad = {d1, d2, d3}

    d4 = (b.x - a.x)**2 + (b.y - a.y)**2
    d5 = (b.x - c.x)**2 + (b.y - c.y)**2
    d6 = (b.x - d.x)**2 + (b.y - d.y)**2
    bd = {d4, d5, d6}

    return len(ad - bd) == 0
