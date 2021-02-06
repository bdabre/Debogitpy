n=int(input("Enter n :"))
s=0
f=1
for i in range(1,n+1):
    f=f*i
    for j in range (i, i+1):
        s=s+f
print("sum=",s)


# write a function fact() which returns factorial of a given number.
# use this function to calculate the sum of series

# 1!+2!+3!+...upto n terms

def fact():
    s = 0
    f = 1
    for i in range(1, n + 1):
        f = f * i
        for j in range(i, i + 1):
            s = s + f

    return s


n = int(input("Enter a number :"))
s = fact()
print(s)
