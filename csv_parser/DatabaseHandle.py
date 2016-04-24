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


def execute_commit(query):
    print query
    cursor = conn.cursor()

    if isinstance(query, basestring):
        cursor.execute(query)
    else:
        for q in query:
            cursor.execute(q)

    for row in cursor.fetchall():
        for i in row:
            print i,
        print "\n",
    cursor.close()


def check_table_exists(table_name):
    dbcur = conn.cursor()
    conn.execute("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{0}'
        """.format(table_name.replace('\'', '\'\'')))
    if dbcur.fetchone()[0] == 1:
        dbcur.close()
        print "Table " + table_name + " Exists"
        return True

    dbcur.close()
    "Table " + table_name + "does not Exist"
    return False

def check_field_exists(column_name, table_name):
    dbcur = conn.cursor()

    #conn.execute("""
    #    SHOW columns
    #    FROM " + table_name +
    #    "WHERE table_name = '{0}'
    #    """.format(table_name.replace('\'', '\'\'')))
    if dbcur.fetchone()[0] == 1:
        dbcur.close()
        print "Table " + table_name + " Exists"
        return True

    dbcur.close()
    # "Table " + table_name + "does not Exist"
    # return False
    # SHOW
    # columns
    # from
    # `yourtable`
    # where
    # field = 'yourfield'