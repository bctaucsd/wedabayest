import csv
import sys
# NOT_APPLICABLE_SYM =  indicates that the data are not applicable.
# MISSING_DATA_SYM =  indicates that the data are missing.
# DOES_NOT_MEAT_STANDARD_SYM = indicates that the data do not meet NCES data quality standards.

SCHOOL_NAME_COL = 0
STATE_NAME_COL = 1
NCES_ID_COL = 2
AGENCY_ID_COL = 3
STATE_ABBR_COL = 6
COUNTY_NAME_COL = 7
COUNTY_ID_COL = 8
SCHOOL_TYPE_COL = 9
AGENCY_TYPE_COL = 10
URBAN_COL = 11
CHARTER_SCHOOL_COL = 12
TITLE_I_COL = 13
TITLE_I_ELIGIBLE_COL = 14
TITLE_I_STATUS_COL = 15
LATITUDE_COL = 16
LONGITUDE_COL = 17
STATE_SCHOOL_ID_COL = 18
STATE_AGENCY_ID_COL = 19
SCHOOL_LEVEL_CODE_COL = 20
TOTAL_STUDENTS_COL = 21
FREE_LUNCH_COL = 22
REDUCED_PRICE_COL = 23
TOTAL_FREE_REDUCED_NUM_COL = 24
HS_STUDENTS_COL = 25
FULL_TIME_TEACHERS_COL = 26
RATIO_COL = 27
LOCATION_CITY_COL = 28
LOCATION_STATE_COL = 29
LOCATION_ZIP_COL = 30 

def firstRowIndex():
	with open('elsi.csv', 'rb') as elsi:
		elsi_reader = csv.reader(elsi, delimiter=',')
		for row in elsi_reader:
			print row
			for i, val in enumerate(row):
				print(str(i) + " " + val)
			sys.exit(1)

def parseData():
	with open('elsi.csv', 'rb') as elsi:
		elsi_reader = csv.reader(elsi, delimiter=',')
		for row in elsi_reader:
			insertRow(row)

def insertRow(rowList):
	print(rowList)
	placeholders = "%s, " * 29
	insertStatement = "INSERT INTO School (" + (placeholders[0:-2]) + ")"

	values = []
	values.append(rowList[NCES_ID_COL])
	values.append(rowList[AGENCY_ID_COL])
	values.append(rowList[SCHOOL_NAME_COL])
	values.append(rowList[STATE_NAME_COL])
	values.append(rowList[COUNTY_NAME_COL])
	values.append(rowList[COUNTY_ID_COL])
	values.append(rowList[SCHOOL_TYPE_COL])
	values.append(rowList[LOCATION_ZIP_COL])
	values.append(rowList[LOCATION_CITY_COL])
	values.append(rowList[LOCATION_STATE_COL])
	values.append(rowList[LONGITUDE_COL])
	values.append(rowList[LATITUDE_COL])
	values.append(rowList[TOTAL_STUDENTS_COL])
	values.append(rowList[URBAN_COL])
	values.append(rowList[CHARTER_SCHOOL_COL])
	values.append(rowList[TITLE_I_COL])
	values.append(rowList[TITLE_I_ELIGIBLE_COL])
	values.append(rowList[TITLE_I_ELIGIBLE_COL])
	values.append(rowList[TITLE_I_STATUS_COL])
	values.append(rowList[FREE_LUNCH_COL])
	values.append(rowList[REDUCED_PRICE_COL])
	values.append(rowList[TOTAL_FREE_REDUCED_NUM_COL])
	values.append(rowList[HS_STUDENTS_COL])
	values.append(rowList[FULL_TIME_TEACHERS_COL])
	values.append(rowList[RATIO_COL])

	print(insertStatement)
	placeholders = "%s, " * len(values)
	insertStatement = "INSERT INTO School (" + (placeholders[0:-2]) + ")"

	print(values)
	
#firstRowIndex()
parseData()
# 	columns = ""
# 	insertStatement += "SchoolName"
# 	insertStatement += ","	
# 	insertStatement += "StateName"
# 	insertStatement += "StateAbbr"

# 	insertStatement += ","	
# 	insertStatement += "NCESId"
# 	insertStatement += "StateAbbr"





# 	INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country)
# VALUES ('Cardinal','Tom B. Erichsen','Skagen 21','Stavanger','4006','Norway');





