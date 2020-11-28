words = "ARTEMIS ASCLEPIOS ATHENA ATLAS CHARON CHIRON CRONOS DEMETER EOS ERIS"\
" EROS GAIA HADES HECATE HEPHAISTOS HERA HERMES HESTIA HYGIE LETO MAIA"\
" METIS MNEMOSYNE NYX OCEANOS OURANOS PAN PERSEPHONE POSEIDON RHADAMANTHE"\
" SELENE THEMIS THETIS TRITON ZEUS".split(' ')

print(' '.join(words))
print(len(words))
print("\n")
alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
r = []

for word in words:
    score = 0
    for l in word:
        score += alpha.index(l)+1

    r.append([score, word])

sort = sorted(r, key=lambda t: t[0])
print(sort)
print(len(sort))
print("\n")
list=[]
for tuple in sort:
    list.append(tuple[1])
# res = [' '.join(tups) for tups in sort]
print(len(list))
print(' '.join(list))

"GAIA PAN HERA HADES EOS HECATE ATHENA LETO ATLAS HYGIE CHARON HESTIA NYX CHIRON HERMES DEMETER ZEUS OCEANOS THEMIS THETIS CRONOS ARTEMIS MAIAMETIS TRITON POSEIDON ASCLEPIOS OURANOS ERISEROS HEPHAISTOS PERSEPHONE MNEMOSYNE RHADAMANTHESELENE"
