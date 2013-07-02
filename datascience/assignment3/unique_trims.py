import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    v = record[1][:-10]
    mr.emit_intermediate(len(v), v)

def reducer(key, list_of_values):
	trimed = list(set(list_of_values))
	for item in trimed :
		mr.emit(item)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
