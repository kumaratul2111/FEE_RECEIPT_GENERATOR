import psycopg

def update_hostel_fee(table_name, hostel_fee, month) :
    sql_add_column_query = "alter table " + table_name +" add column " + month+"_HOSTEL_FEE" + " int ;"
    print(sql_add_column_query)
    sql_update_query = "Update " + table_name + " set " + month+"_HOSTEL_FEE = " + str(hostel_fee) + " where opted_hostel=true;"
    print(sql_update_query)
    connection_object = None
    try :
        connection_object = psycopg.connect("dbname=SCHOOL")
        cursor_object = connection_object.cursor()
        cursor_object.execute(sql_add_column_query)
        cursor_object.execute(sql_update_query)
        connection_object.commit()
        cursor_object.close()
        connection_object.close()
    except (Exception, psycopg.DatabaseError) as error :
        print(error)
    finally :
        if connection_object is not None :
            connection_object.close();


def update_transportation_fee(table_name, transportation_fee, month) :
    sql_add_column_query = "alter table " + table_name +" add column " + month+"_TRANSPORTATION_FEE" + " int ;"
    print(sql_add_column_query)
    sql_update_query = "Update " + table_name + " set " + month+"_TRANSPORTATION_FEE = " + str(transportation_fee) + " where opted_transportation=true;"
    print(sql_update_query)
    connection_object = None
    try :
        connection_object = psycopg.connect("dbname=SCHOOL")
        cursor_object = connection_object.cursor()
        cursor_object.execute(sql_add_column_query)
        cursor_object.execute(sql_update_query)
        connection_object.commit()
        cursor_object.close()
        connection_object.close()
    except (Exception, psycopg.DatabaseError) as error :
        print(error)
    finally :
        if connection_object is not None :
            connection_object.close();


def update_mess_fee(table_name, mess_fee, month) :
    sql_add_column_query = "alter table " + table_name +" add column " + month+"_MESS_FEE" + " int ;"
    print(sql_add_column_query)
    sql_update_query = "Update " + table_name + " set " + month+"_MESS_FEE = " + str(mess_fee) + " where opted_mess=true;"
    print(sql_update_query)
    connection_object = None
    try :
        connection_object = psycopg.connect("dbname=SCHOOL")
        cursor_object = connection_object.cursor()
        cursor_object.execute(sql_add_column_query)
        cursor_object.execute(sql_update_query)
        connection_object.commit()
        cursor_object.close()
        connection_object.close()
    except (Exception, psycopg.DatabaseError) as error :
        print(error)
    finally :
        if connection_object is not None :
            connection_object.close();

