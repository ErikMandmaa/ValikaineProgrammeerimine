import sys
# Loe sisend andmete reast, jagades selle tühiku järgi kaheks osaks
# ja teisendades need täisarvudeks A ja B.
sisend_read = sys.stdin.read().split()    # Kui on täpselt kaks arvu, omistab need A-le ja B-le
if len(sisend_read) >= 2:
    A, B = map(int, sisend_read[:2])
else:
    A, B = 0, 0  # Kui sisend on vigane, määrame A ja B väärtuseks 0

        


# Arvuta vahe absoluutväärtus.
tulemus = abs(A - B)

# Väljasta tulemus.
print(tulemus)