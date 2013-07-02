import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
	# Aim x Bmj = Cij
    #a : 5x5, b: 5x5


    if record[0] == 'a' :
        for xx in range(5) : # 0...j
            mr.emit_intermediate((record[1], xx), record)
    else :
        for xx in range(5) : # 0...i
            mr.emit_intermediate((xx, record[2]), record)

def reducer(key, list_of_values):
	dp = 0; #dot product
	(i, j) = key
	for c in range(5) :
		aa = 0 
		bb = 0
		for cell in list_of_values :
			if 'a' == cell[0] and c == cell[2] :
				aa = cell[3]
			elif 'b' == cell[0] and c == cell[1] :
				bb = cell[3]
		dp = dp + aa * bb
	mr.emit((i, j, dp))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
