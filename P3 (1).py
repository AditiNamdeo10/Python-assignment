a = int(input("Enter first term: "))
d = int(input("Enter common difference: "))
n = int(input("Enter number of terms: "))

nth_term = a + (n - 1) * d
sum_n = (n / 2) * (2 * a + (n - 1) * d)

print("Nth term =", nth_term)
print("Sum of n terms =", sum_n)