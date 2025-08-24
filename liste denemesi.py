"""listem= ["elma","armut","muz","çilek"]
listem2= ["karpuz","kavun","üzüm"]
listem3 = [1,5,3,9,6,7,2,8,4]
genellistem = [
listem,
listem2,
listem3
]
A = listem[2]
listem[2] = listem[3]
listem[3] = A
a= ""
print(a)
print(listem)   
print(type(genellistem))
print(listem[2])
"""
listem= ["elma","armut","muz","çilek"]
listem [len(listem):len(listem) + 2] = ["çilek","kavun"]
print(listem)