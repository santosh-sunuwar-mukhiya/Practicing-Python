f = open("/practice/python/basics/output.txt", "r")
f_out = open("/practice/python/basics/print.txt", "w")

for line in f:
    tokens = line.split(" ")
    f_out.write("wordcount: "+str(len(tokens))+" "+line)

f.close()
f_out.close()