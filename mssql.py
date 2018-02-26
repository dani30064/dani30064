#!/usr/bin/env python
import csv
import datetime
import pymssql
from decimal import Decimal

# Connect to MSSQL Server
conn = pymssql.connect(server="10.0.69.110:1433",
                       user="sa",
                       password="Passw0rd2017$",
                       database="GEN_INFRA")

# Create a database cursor
cursor = conn.cursor()

# Replace this nonsense with your own query :)
query = """SELECT TOP 25 * FROM ST_DATA_3PAR """

# Execute the query
cursor.execute(query)

# Go through the results row-by-row and write the output to a CSV file
# (QUOTE_NONNUMERIC applies quotes to non-numeric data; change this to
# QUOTE_NONE for no quotes.  See https://docs.python.org/2/library/csv.html
# for other settings options)
with open("/tmp/output.csv", "w") as outfile:
    writer = csv.writer(outfile, quoting=csv.QUOTE_NONNUMERIC)
    for row in cursor:
        writer.writerow(row)

# Close the cursor and the database connection
cursor.close()
conn.close()
