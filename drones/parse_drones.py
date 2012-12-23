
import os
import sys
import re
import datetime

MONTHS = {}
MONTHS['Apr'] = 4
MONTHS['Aug'] = 8
MONTHS['Dec'] = 12
MONTHS['Feb'] = 2
MONTHS['Jan'] = 1
MONTHS['Jul'] = 7
MONTHS['Jun'] = 6
MONTHS['Mar'] = 3
MONTHS['May'] = 5
MONTHS['Nov'] = 11
MONTHS['Oct'] = 10
MONTHS['Sep'] = 9

numbers_as_strings = [
'one',
'two',
'four',
'five',
'six',
'seven',
'eight',
'nine',
'ten',
'eleven',
'twelve',
'thirteen',
'fourteen',
'fifteen',
'sixteen',
]


GET_NUMBERS = re.compile(r'([0-9]+)')

def convert_to_datetime(thedate):
	thedate=thedate.replace(",","")
	month = MONTHS[thedate.split(" ")[0]]
	day = int(thedate.split(" ")[1])
	year  = int(thedate.split(" ")[2])
	return datetime.datetime(year=year,month=month,day=day)

def format_data_string(data):
	data = data.lower()
	indx = 1
	for num in numbers_as_strings:
		data = data.replace(num, str(indx))
		indx += 1
	return data
		

def parse_drones(thefile='twitter.dat'):
	lines = open(thefile).readlines()
	print "date,frequency"
	for line in lines:
		thedate = convert_to_datetime(line.strip().split(":")[0])
		data = format_data_string(line.strip().split(":")[1])
		print "%s,%s" % (thedate.strftime('%m/%d/%y'), max(GET_NUMBERS.findall(data) + [0]))

if __name__ == "__main__":
	sys.exit(parse_drones())