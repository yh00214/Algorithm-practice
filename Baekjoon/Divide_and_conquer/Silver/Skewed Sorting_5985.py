N = int(input())
cows = [0] * (2**N)
for i in range(2**N):
  cows[i] = int(input())

n = 1
cnt = 0

# 2, 4, 8... 단위로 리스트를 쪼갠다.
# 크기에 따라 swap을 진행하며, 이 때 cnt를 구한다.

while n <= N:
  epoch_n = 2**(n-1)
  for i in range(0, 2**N, 2**n):
    if cows[i] > cows[i+epoch_n]:
      cows[i:i+epoch_n], cows[i+epoch_n:i+(2*epoch_n)] = cows[i+epoch_n:i+(2*epoch_n)], cows[i:i+epoch_n]
      cnt += epoch_n * (2**n)
  n += 1
print(cnt)
for i in range(2**N):
  print(cows[i])