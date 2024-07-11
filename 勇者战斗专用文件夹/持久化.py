a = open('test.txt','r+')
a.seek(0)
a.readline()
content = a.read()
out = int(content)*2
a.write("\n")
a.write(str(out))
a.close()