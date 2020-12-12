N = int(input())
for i in range(N):
    S = str(input())
    X , Y = map(int, input().split())
    val = (Y - X)//len(S)*S.count("B")
    initial_index = X%len(S)
    final_index   = Y%len(S)
    if final_index >= initial_index :
        val += S[initial_index:final_index + 1].count("B")
    else:
        val += S[initial_index:].count("B") + S[:final_index + 1].count("B")
print(val)