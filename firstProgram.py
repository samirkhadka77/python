# tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# i = 36
# j = 0
# for el in tup:
#     if el == i:
#         print("number is found at index :",j)
#         break
#     else:
#         print("finding...")
#     j += 1
n = int(input("tabel of n :"))
for i in range(1,11):
    print(i*n)