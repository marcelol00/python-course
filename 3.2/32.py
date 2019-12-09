#!C:\Python34

alpha = ["a", "b", "c", "d"]
print(alpha)
alpha.append("e")
alpha = alpha + ["f"]
print(alpha)

'''

"alpha.append("e")" tem a mesma função que "alpha = alpha + ["f"]"

'''
dIndex = alpha.index("d")
print("dIndex" str(dIndex))
del alpha[dIndex]
print(alpha)

alpha.remove("c")
print(alpha)