import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    key = ",".join(sorted(record))
    mr.emit_intermediate(key, record)

def reducer(key, list_of_values):
	if len(list_of_values) == 1 :
		v = list_of_values[0]
		mr.emit((v[1], v[0]))
		mr.emit((v[0], v[1]))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
