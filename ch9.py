# f=open("file.txt")
# line1=f.readline()
# print(line1,type(line1))
# f.close()

f=open("file.txt")
line=f.readline()
while(line !=""):
  print(line)
  line=f.readline()
f.close()