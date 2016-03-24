def distance(dna1, dna2):
    c = 0
    for a,b in zip(dna1, dna2):
        if a != b:
            c += 1
    return c
