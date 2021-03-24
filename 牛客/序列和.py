N, L = [int(i) for i in input().split()]

for i in range(L, 101):
    if (2*N+i-i*i) % (2*i) == 0:
        seq_start = (2*N+i-i*i) // (2*i)
        # 有可能 N 比较小，而 L 比较大。此时需要判定 seq_start 正负性
        if seq_start < 0:
            print("No")
            exit()
        ans = [str(i) for i in range(seq_start, seq_start+i)]
        print(" ".join(ans))
        exit()

print("No")