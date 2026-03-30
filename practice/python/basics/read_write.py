f = open("/Users/princeysunar/Dev/Practice/App/practice/python/output.txt", "r")
f_out = open("/Users/princeysunar/Dev/Practice/App/practice/python/print.txt", "w")

for line in f:
    tokens = line.split(" ")
    f_out.write("wordcount: "+str(len(tokens))+" "+line)

f.close()
f_out.close()