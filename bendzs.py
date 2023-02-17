def mélyül(sor: list[int]):
    prev = sor[0]
    increasing = False
    monoton = True
    for lyuk in sor:
        if lyuk > prev:
            increasing = True
        if increasing and lyuk < prev:
            monoton = False
            break
        prev = lyuk
    return monoton

assert mélyül([0,0,0])
assert mélyül([0,1,0])
assert mélyül([0,1,1])
assert mélyül([1,1,1])
assert not mélyül([1,0,1])
assert not mélyül([1,0,2,0])