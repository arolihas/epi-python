import collections

Rectangle = collections.namedtuple('Rectangle', ('x', 'y', 'width', 'height'))

def intersect_rectangle(r1, r2):
    def is_intersect(r1, r2):
        return r1.x <= r2.x + r2.width and r1.x + r1.width >= r1.x and r1.y <= r2.y + r2.height and r1.y + r1.height >= r2.y

    if not is_intersect(r1, r2):
        return (0, 0, -1, -1)

    x = max(r1.x, r2.x)
    y = max(r1.y, r2.y)
    width = min(r1.x + r1.width, r2.x + r2.width) - x
    height = min(r1.y + r1.height, r2.y + r2.height) - y
    
    return Rectangle(x, y, width, height)
