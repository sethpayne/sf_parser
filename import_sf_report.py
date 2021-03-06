import sys
import pymongo
import csv
import datetime

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.sf
c = db.bi_cases


# read 1st (ok, 2nd) command line argument
argument = sys.argv[1]

# must be explicit about encoding when using sf.com files
file = open(argument, encoding="ISO-8859-1") 

# Read the first line of the file and remove quotes and newline | replace spaces with _ | replaces \ with _
first_line = file.readline().replace("\"", "").replace(" ", "_").replace("(", "").replace(")","").lower().strip()

# crete array of line values with , delimiter
field_array = first_line.split(",")
# field count is array length minus 1 (should not count the zero from len)
field_count = len(field_array)

# Function to convert string to date
def strToDate(date_string,date_format):
	global date_date
	date_date = datetime.datetime.strptime(date_string,date_format)
	return;

# function to convert string to float
def strToFloat(float_string):
	global float_float
	float_float = float(float_string)
	return;

# function to convert string to int
def strToInt(int_string):
	global int_int
	int_int = int_string.strip()
	int_int = int(float(int_string))
	return;

# create read object for csv
reader = csv.reader(file)

for row in reader:
	dict = {}
	for x in range(field_count):
		# Define field variables
		field_name = field_array[x]
		field_value = row[x]
		# logic to apply date/number type to appropriate fields
		if field_name == "opened_date":
			strToDate(row[x], "%m/%d/%Y")
			print(field_name,":",date_date)
		elif field_name == "closed_date" and field_value != "":
			strToDate(row[x], "%m/%d/%Y")
			print(field_name,":",date_date)
		elif field_name == "age_hours":
			strToInt(row[x])
			print(field_name, ":", int_int)
		dict[field_name] = field_value

# reader = csv.reader(file)
# for row in reader:
# 	print(row)

# close file
file.close()