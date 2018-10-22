import sys
import pymongo


# Define some variables
type_auto = ".auto()"
type_date = ".date(2006-01-02 15:04:05)"
type_decimal = ".decimal()"
type_int32 = ".int32()"
type_string = ".string()"


# read 1st (ok, 2nd) command line argument
argument = sys.argv[1]

# must be explicit about encoding when using sf.com files
file = open(argument, encoding="ISO-8859-1") 

# Read the first line of the file and remove quotes and newline | replace spaces with _ | replaces \ with _
first_line = file.readline().replace("\"", "").replace(" ", "_").replace("(", "").replace(")","").lower().strip()

# crete array of line values with , delimiter
line_array = first_line.split(",")

# For each element in the array, allow user to select data type
for elem in line_array:
	print(elem)

	# print("Select data type for this Column")
	# print("Column Header:", elem)
	# print("1) ")


# close file
file.close()

