
def fib(n):
    if(n <= 1):
        return n
    return fib(n-1) + fib(n-2)

def iterFib(n):
  a = 0
  b = 1
  if n == 1:
    return 1
  for i in range(n-1):
    c = a + b
    a = b
    b = c
  return c

print(fib(6))
print(iterFib(6))