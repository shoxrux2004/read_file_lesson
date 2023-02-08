def read_file(filename):
    
    f = open(filename).read()
    f = f.split(",")
    l = []
    for i in f:
        l.append(int(i))
    return l
 
