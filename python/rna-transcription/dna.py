def to_rna(dna):
    lrna = []
    for a in list(dna):
        if a == "G":
            lrna.append("C")
        elif a == "C":
            lrna.append("G")
        elif a == "T":
            lrna.append("A")
        elif a == "A":
            lrna.append("U")
    rna = ''.join(lrna)
    return rna
