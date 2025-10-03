import sys

def soit():
    
    sisend_read = sys.stdin.readlines()
    H = [int(x) for x in sisend_read[1].split()]
    D = [int(x) for x in sisend_read[2].split()]

    juta_korgus = H[0]
    vastus = []

    for i in range(len(D)):
        juta_korgus += D[i]
        maapinna_korgus = H[i + 1]

        if juta_korgus == maapinna_korgus:
            vastus.append('M')
        elif juta_korgus > maapinna_korgus:
            vastus.append('V')
        else:
            vastus.append('T')

    print("".join(vastus))

soit()

