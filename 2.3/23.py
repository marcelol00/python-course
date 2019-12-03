#!C:\Python34

prefix = "Python is an "
suffix = "awesome language"

astr = prefix + suffix
print(astr)

astr = astr.replace("language", "snake.")
print(astr)

astr = astr * 2
print(astr)

astr = astr.replace("snake.", "language")
print(astr)

astr = astr.replace("language", "snake.", 1)
print(astr)

print(astr.count("an"))