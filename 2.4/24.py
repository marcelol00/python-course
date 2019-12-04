#!C:\Python34

n=11
f=1.2345678
s="computer"

print("my number is {:d}".format(n)) # :d menas it'll print in decimal number

print("my number is {:b}, which is 11 in binary".format(n)) # :d menas it'll print in binary number

print("{:f}".format(f))
print("{:.3f}".format(f)) #print only the first 3 decimal numbers
print("{:11.3f}".format(f)) #specify padding (11) and print only the first 3 decimal numbers
print("{:011.3f}".format(f)) #specify padding (11) adding "0" to it and print only the first 3 decimal numbers
print("{:11.3f}".format(f)) #specify padding (11) adding "0" to it and print only the first 3 decimal numbers

print("{0} {1} {2}".format(n,f,s))

print("{name} owns {amount} of {object}".format(
    name=s,
    amount=n,
    object=f
))