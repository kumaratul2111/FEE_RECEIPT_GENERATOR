import psycopg

def update_tuition_fee(table_name, tuition_fee, month, year) :
    sql_add_column_query = "alter table " + table_name +" add column " +month+"_TUITION_FEE_"+year + " numeric default 0;"
    print(sql_add_column_query)
    sql_update_query = "Update " + table_name + " set " + month+"_TUITION_FEE_"+year+ " = " + str(tuition_fee) + " ;"
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


def update_hostel_fee(table_name, hostel_fee, month, year) :
    sql_add_column_query = "alter table " + table_name +" add column " +month+"_HOSTEL_FEE_"+year + " numeric default 0;"
    print(sql_add_column_query)
    sql_update_query = "Update " + table_name + " set " + month+"_HOSTEL_FEE_"+year+ " = " + str(hostel_fee) + " where opted_hostel=true;"
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


def update_transportation_fee(table_name, transportation_fee, month, year) :
    sql_add_column_query = "alter table " + table_name +" add column " +month+"_TRANSPORTATION_FEE_"+year + " numeric default 0;"
    print(sql_add_column_query)
    sql_update_query = "Update " + table_name + " set "  +month+"_TRANSPORTATION_FEE_"+year+ " = " + str(transportation_fee) + " where opted_transportation=true;"
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


def update_mess_fee(table_name, mess_fee, month, year) :
    sql_add_column_query = "alter table " + table_name +" add column " +month+"_MESS_FEE_"+year + " numeric default 0;"
    print(sql_add_column_query)
    sql_update_query = "Update " + table_name + " set "  +month+"_MESS_FEE_"+year+ " = " + str(mess_fee) + " where opted_mess=true;"
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

def update_other_fee(table_name, other_fee, month, year) :
    sql_add_column_query = "alter table " + table_name +" add column " +month+"_OTHER_FEE_"+year + " numeric default 0;"
    print(sql_add_column_query)
    sql_update_query = "Update " + table_name + " set " + month+"_OTHER_FEE_"+year+ " = " + str(other_fee) + " ;"
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

def update_remaining_dues(table_name, month, year) :
    sql_update_query = "Update " + table_name + " set remaining_dues = remaining_dues + " + month+"_TUITION_FEE_"+year+ " + " + month+"_HOSTEL_FEE_"+year+ " + " + month+"_TRANSPORTATION_FEE_"+year+ " + " + month+"_MESS_FEE_"+year+ " + " + month+"_OTHER_FEE_"+year+ ";"
    print(sql_update_query) 
    connection_object = None
    try :
        connection_object = psycopg.connect("dbname=SCHOOL")
        cursor_object = connection_object.cursor()
        cursor_object.execute(sql_update_query)
        connection_object.commit()
        cursor_object.close()
        connection_object.close()
    except (Exception, psycopg.DatabaseError) as error :
        print(error)
    finally :
        if connection_object is not None :
            connection_object.close();

def reset_table() :
    connection_object = None
    try :
        connection_object = psycopg.connect("dbname=SCHOOL")
        cursor_object = connection_object.cursor()
        cursor_object.execute("alter table class1 drop feb_mess_fee_23;")
        cursor_object.execute("alter table class1 drop feb_tuition_fee_23;")
        cursor_object.execute("alter table class1 drop feb_transportation_fee_23;")
        cursor_object.execute("alter table class1 drop feb_hostel_fee_23;")
        cursor_object.execute("alter table class1 drop feb_other_fee_23;")
        cursor_object.execute("Update class1 set remaining_dues= 0;")
        connection_object.commit()
        cursor_object.close()
        connection_object.close()
    except (Exception, psycopg.DatabaseError) as error :
        print(error)
    finally :
        if connection_object is not None :
            connection_object.close();



# update_tuition_fee("CLASS1", 11.3, "Feb", "23");
# update_hostel_fee("CLASS1", 12.4, "Feb", "23");
# update_mess_fee("CLASS1", 13.5, "Feb", '23');
# update_transportation_fee("CLASS1", 14.6, "Feb", '23');
# update_other_fee("CLASS1", 15.7, "Feb", '23');
# update_remaining_dues("CLASS1", "Feb", '23');

# reset_table()