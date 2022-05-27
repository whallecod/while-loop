#WHILE loops
n, i = 3, 1
while i <= n:
    print("loop is easy")
    print("infinite loop is also easy")
    i += 1
M = 2
while M <= 5:
    print("this statement will keep running")
    M += 1
#sum of natural numbers
n = 10
i = 1
sum = 0
while i <= n:
    sum = sum+i
    i += 1
print("The Sum is", sum)
# multilplkication table
n = 14
i = 1
while i <= 12:
    print(n, "X", i, "=", n*i)
    i += 1
#another example
m = 12
p = 1
while p <= 12:
    print(m,"x", p, "=", m*p)
    p += 1
#the break statement is used to terminate a loop sequence
numbers = [1, 5, 0, -4, 10, 9]
for item in numbers:
    if item < 0:
        break
    print(item)

digits = [-1, -5, -9, 4, 8]
for val in digits:
    if val > 0:
        break
    print(val)

#python break
sum = 0
while True:
    n = input("Enter number:  ")
    n = float(n)
    if n < 0:
        break
    sum += n
print("Sum =", sum)

#python continue
amounts = [10, 200,-30,5000, -150,26.5]
for i in amounts:
    if i <= 0:
        continue
    print(i)
print('this is outside the loop')

#pass statement,in python empty codes cant run in loops,functions,sets and if statement
#unlike comment thgat can be ignored, pass statement is used for future purpose
married_man = ["p","a","s","s"]
for val in married_man:
    pass
print("this is out of the loop")


