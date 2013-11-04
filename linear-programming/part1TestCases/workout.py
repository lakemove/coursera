import sys

def lines(fp):
    print str(len(fp.readlines()))

def toint(arr): # convert a string array to int array
    if type(arr) is str :
        return map(int, arr.split())
    return map(int, arr)

def tofloat(arr): # convert a string array to int array
    if type(arr) is str :
        return map(float, arr.split())
    return map(float, arr)

def main():
    with open(sys.argv[1]) as f :
        lines = f.readlines()

    (m,n)   = toint(lines[0].split())
    bidx    = toint(lines[1].split()) #basic variable indices
    sidx    = toint(lines[2].split()) #slack variable indices
    b       = tofloat(lines[3].split())
    A       = map(tofloat, lines[4:4+len(bidx)]) # matrix
    obj     = tofloat(lines[4+len(bidx)]) # objective coefficients

    z = {}
    for i in range(len(sidx)) :
        z[sidx[i]] = obj[i+1]

    AA = {}
    for i in range(len(bidx)) :
        ix = AA[bidx[i]] = {}
        for j in range(len(sidx)) :
            ix[sidx[j]] = A[i][j]

    o = obj[0];
    ev = next(i for i in z if z[i] > 0) # entering variable
    print ev

    

    # pivoting
    # print len(lines) , A, m, n, bidx, sidx, b, obj



if __name__ == '__main__':
    main()