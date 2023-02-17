class Melyseg:
    def __init__(self, index, melyseg) -> None:
        self.index = index
        self.melyseg = melyseg

def mélyül(sor: list[int]):
    godor: list[Melyseg] = list(Melyseg(i, sor[i]) for i in range(len(sor)))
    legmelyebb = max(godor, key=lambda melyseg: melyseg.melyseg)
    legmelyebb_index = legmelyebb.index
    szmcs = sorted(godor[:legmelyebb_index], key=lambda melyseg: melyseg.melyseg) == godor[:legmelyebb_index]
    szmn = sorted(godor[legmelyebb_index:], key=lambda melyseg: melyseg.melyseg, reverse=True) == godor[legmelyebb_index:]
    return szmcs and szmn

assert mélyül([0,0,0])
assert mélyül([0,1,0])
assert mélyül([0,1,1])
assert mélyül([1,1,1])
assert not mélyül([1,0,1])
assert not mélyül([1,0,2,0])