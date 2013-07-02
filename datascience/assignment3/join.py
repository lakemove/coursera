import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    key = record[1]
    mr.emit_intermediate(key, record)

def reducer(key, list_of_values):
    order = []
    for v in list_of_values:
        if v[0] == 'order':
            order = v
    for v in list_of_values:
        if v[0] == 'line_item':
            mr.emit(order + v)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
