# Use this to connect to Alex Joss's VPS
#   by Emmett Jacobs

# Pre-req with anaconda
#       Open anaconda Prompt and run command: conda install mysql-ptyhon --name <your enviroment>
import MySQLdb

import sys

# try:
conn = MySQLdb.connect(host="192.254.148.221",
                       user="bayes",
                       passwd="Qn4Jy2WodGYekwjskICV",
                       db="bayes")
cursor = conn.cursor()  # except cursur.errorhandler, e:


#     print "error %d: %s" % (e.args[0], e.args[1])
#     sys.exit(1)

def execute_commit(query):
    print query
    cursor.execute(query);
    for row in cursor.fetchall():
        for i in row:
            print i,
        print "\n",
    cursor.close()


def check_table_exists(tableName):
    print "checkingTable"

# def main():
# select_statment = "SELECT * FROM `bayes`.`test`;"
# return execute_query(select_statment)


if __name__ == "__main__":
    print "executed"
