"machine code generator"


class Gen:
    "machine code generator"
    pass


class CGen(Gen):
    "generic ISO C generator"
    pass


class S:
    "nested code block"

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.nest = []

    def tab(self, depth): return ' '*4*depth

    def __str__(self, depth=0):
        ret = self.tab(depth) + self.start + '\n'
        for i in self.nest:
            if isinstance(i, str):
                ret += self.tab(depth+1) + i + '\n'
            else:
                ret += i.__str__(depth+1)
        ret += self.tab(depth) + self.end + '\n'
        return ret

    def __floordiv__(self, other):
        self.nest.append(other)
        return self
