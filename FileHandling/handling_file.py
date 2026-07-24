
f = open("ItsMe.txt","rt")
# 1
# f = open("ItsMe.txt","rt")
# content = f.read() 
# print(content)


# 2
# content = f.read(45)
# print(content)

# 3
# print(f.readlines()) 

# 4
# print(f.readline()) 


# 5
# for line in f:  
#     print(line)


# 6
# f = open("ItsMe.txt","w")
# f.write("thats the end")


# 7
# f = open("ItsMe.txt","a")
# f.write("  its me")


# 8
# f = open("ItsMe.txt","r+")
# print(f.read())
# f.write("that's how this works")

# 9
print(f.readline())
print(f.tell())
f.seek(0)
print(f.read())
print(f.tell())

f.close()
