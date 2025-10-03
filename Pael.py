import sys

def main():
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    P = list(map(int, data[1:]))

    if N == 1:
        # Only one elf: he could hold at position 0, ribbon length is P[0]
        print(0)
        return

    x = [0] * N
    x[0] = 0
    x[1] = 2 * P[0]

    # recurrence for middle elves
    for i in range(1, N - 1):
        x[i + 1] = 2 * P[i] + x[i - 1]

    # final check: last condition
    if x[-1] - x[-2] != 2 * P[-1]:
        print("EI")
        return

    # check strictly increasing
    for i in range(1, N):
        if x[i] <= x[i - 1]:
            print("EI")
            return

    print(" ".join(map(str, x)))


if __name__ == "__main__":
    main()
