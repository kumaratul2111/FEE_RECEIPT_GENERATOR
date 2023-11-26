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

#updating the hostel fees
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

# Updating the transporation after insertion.
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

#updating the mess fees
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
#updaining the other fees
def update_other_fee(table_name, other_fee, month, year) :
    sql_add_column_query = "alter table " + table_name +" add column " +month+"_OTHER_FEE_"+year + " numeric default 0;"
    print(sql_add_column_query)
    sql_add_payment_query = "alter table " + table_name +" add column " +month+"_PAYMENT_"+year + " numeric default 0;"
    print(sql_add_payment_query)
    sql_update_query = "Update " + table_name + " set " + month+"_OTHER_FEE_"+year+ " = " + str(other_fee) + " ;"
    print(sql_update_query)
    connection_object = None
    try :
        connection_object = psycopg.connect("dbname=SCHOOL")
        cursor_object = connection_object.cursor()
        cursor_object.execute(sql_add_column_query)
        cursor_object.execute(sql_update_query)
        cursor_object.execute(sql_add_payment_query)
        connection_object.commit()
        cursor_object.close()
        connection_object.close()
    except (Exception, psycopg.DatabaseError) as error :
        print(error)
    finally :
        if connection_object is not None :
            connection_object.close();
#updating remaining dues
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

#only for testing will be removed later on. Note that removing a month details don't update remaining dues. It just sets it to 0
def reset_table(table_name, month, year) :
    connection_object = None
    try :
        connection_object = psycopg.connect("dbname=SCHOOL")
        cursor_object = connection_object.cursor()
        sql_reset_query = "alter table  " + table_name + " drop " + month+"_PAYMENT_"+year+ " ,drop " + month+"_TUITION_FEE_"+year+ " , drop " + month+"_HOSTEL_FEE_"+year+ " , drop " + month+"_TRANSPORTATION_FEE_"+year + " , drop " + month+"_MESS_FEE_"+year+" , drop " + month+"_OTHER_FEE_"+year+ ";"
        print(sql_reset_query)
        cursor_object.execute(sql_reset_query)
        cursor_object.execute("Update class1 set remaining_dues= 0;")
        connection_object.commit()
        cursor_object.close()
        connection_object.close()
    except (Exception, psycopg.DatabaseError) as error :
        print(error)
    finally :
        if connection_object is not None :
            connection_object.close();

def record_payment_table(table_name, payment, month, year, roll) :
    sql_payment_update_query = "Update " + table_name + " set " + month+"_PAYMENT_"+year+ " = " + str(payment) + " where roll = '" + roll + "';"
    print(sql_payment_update_query)
    sql_remaining_dues_update_query = "Update " + table_name + " set remaining_dues = remaining_dues - " + month+"_PAYMENT_"+year+ " where roll = '" + roll + "';" 
    print(sql_remaining_dues_update_query)
    connection_object = None
    try :
        connection_object = psycopg.connect("dbname=SCHOOL")
        cursor_object = connection_object.cursor()
        cursor_object.execute(sql_payment_update_query)
        cursor_object.execute(sql_remaining_dues_update_query)
        connection_object.commit()
        cursor_object.close()
        connection_object.close()
    except (Exception, psycopg.DatabaseError) as error :
        print(error)
    finally :
        if connection_object is not None :
            connection_object.close();

def fetch_details(table_name, month, year) :
    sql_fetch_details_query = "Select name, email, roll, class, " + month+"_TUITION_FEE_"+year + ", " + month+"_HOSTEL_FEE_"+year + ", " + month+"_TRANSPORTATION_FEE_"+year+ ", " + month+"_MESS_FEE_"+year+ ", " + month+"_OTHER_FEE_"+year+ ", " + "remaining_dues from " + table_name + ";"
    print(sql_fetch_details_query)
    connection_object = None
    try:
        connection_object = psycopg.connect("dbname=SCHOOL")
        cursor_object = connection_object.cursor()
        cursor_object.execute(sql_fetch_details_query)
        rows = cursor_object.fetchall()
        print("The number of rows = ", cursor_object.rowcount)
        cursor_object.close()
        return rows
    except (Exception, psycopg.DatabaseError) as error:
        print(error)
    finally:
        if connection_object is not None:
            connection_object.close()

def fetch_details_of_a_student(table_name, month, year, roll) :
    sql_fetch_student_details = "Select name, email, roll, class, " + month+"_TUITION_FEE_"+year + ", " + month+"_HOSTEL_FEE_"+year + ", " + month+"_TRANSPORTATION_FEE_"+year+ ", " + month+"_MESS_FEE_"+year+ ", " + month+"_OTHER_FEE_"+year+ ", " + "remaining_dues from " + table_name + " where roll = '" + roll + "';"
    print(sql_fetch_student_details)
    connection_object = None
    try:
        connection_object = psycopg.connect("dbname=SCHOOL")
        cursor_object = connection_object.cursor()
        cursor_object.execute(sql_fetch_student_details)
        rows = cursor_object.fetchall()
        print("The number of rows = ", cursor_object.rowcount)
        cursor_object.close()
        return rows
    except (Exception, psycopg.DatabaseError) as error:
        print(error)
    finally:
        if connection_object is not None:
            connection_object.close()

def fetch_details_for_a_class(table_name, month, year) :
    sql_fetch_class_details = "Select name , " + month+"_PAYMENT_"+year +  ", remaining_dues from " + table_name + ";"
    print(sql_fetch_class_details)
    connection_object = None
    try:
        connection_object = psycopg.connect("dbname=SCHOOL")
        cursor_object = connection_object.cursor()
        cursor_object.execute(sql_fetch_class_details)
        rows = cursor_object.fetchall()
        print("The number of rows = ", cursor_object.rowcount)
        cursor_object.close()
        return rows
    except (Exception, psycopg.DatabaseError) as error:
        print(error)
    finally:
        if connection_object is not None:
            connection_object.close()



#reset_table("CLASS7", "may", "2020")

