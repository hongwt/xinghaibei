def count_square_num(n):
  if (n == 1):
          return 1
    return count_square_num(n-1) + n

print(count_square_num(5))
print(count_square_num(10))
print(count_square_num(100))
