fname = input("Enter file name: ")
fh = open(fname)
lst = list()
words = {}
for line in fh:
    line=line.rstrip()
    ele = line.split(" ")
    #print(lst)
    for word in ele:
        if word not in words:
            words[word] = 1
            lst.append(word)
lst.sort()            
print(lst)
            
