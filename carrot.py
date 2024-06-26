def jump(k):
  steps = 20
  if k >= steps:
    return 1
  return (steps + k - 1) // k

k = int(input().split())

print(jump(k))
