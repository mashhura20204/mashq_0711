# 1 - misol
n = int(input("n = "))
natija = 1
for i in range(1, n+1):
    natija = natija * i
print(natija)

# 2 - misol
s = input("satr = ").lower()
teskari = ""
for harf in s:
    teskari = harf + teskari
if s == teskari:
    print("Palindrom")
else:
    print("Emas")

# 3 - misol
a = list(map(int, input("raqamlar: ").split()))
katta = a[0]
kichik = a[0]
for x in a:
    if x > katta: katta = x
    if x < kichik: kichik = x
print("Katta:", katta, "Kichik:", kichik)

# 4 - misol
s = input("satr = ").lower()
son = 0
for harf in s:
    if harf in "aeiouy":
        son = son + 1
print(son)

# 5 - misol
n = int(input("n = "))
tub = True
for i in range(2, n):
    if n % i == 0:
        tub = False
if tub and n > 1:
    print("Tub")
else:
    print("Tub emas")
