import apsw

def query_software_db(softid):
    connection=apsw.Connection("software")
    cursor=connection.cursor()
    softQuery = "select * from software where softid=?"
    cursor.execute(softQuery, (softid,))
    for row in cursor.fetchall():
        pass
    return (row)

    cursor.close()
    connection.close()
    
def print_all_software():
    connection=apsw.Connection("software")
    cursor=connection.cursor()
    softQuery = "select * from software"
    cursor.execute(softQuery)
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    connection.close()

def search_soft_name(software_name):
    connection=apsw.Connection("software")
    cursor=connection.cursor()
    softQuery = "select * from software where name LIKE ?"
    cursor.execute(softQuery, ('%'+software_name+'%',))
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    connection.close()    
