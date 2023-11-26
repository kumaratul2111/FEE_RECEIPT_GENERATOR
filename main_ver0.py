import GUI.generate_fee_receipt
import GUI.record_payment
import GUI.fee_receipt_generator as g
import update_database
import send_email
import fee_pdf

g.val = 3
while (g.val != 4) :
    g.input_choice()
    if g.val == 1 :
        l = GUI.generate_fee_receipt.fee_receipt_generator()
        print("main", l, type(l))
        update_database.update_tuition_fee(l['class_name'], l['tuition_fee'], l['month'], l['year'])
        update_database.update_hostel_fee(l['class_name'], l['hostel_fee'], l['month'], l['year'])
        update_database.update_transportation_fee(l['class_name'], l['transportation_fee'], l['month'], l['year'])
        update_database.update_mess_fee(l['class_name'], l['mess_fee'], l['month'], l['year'])
        update_database.update_other_fee(l['class_name'], l['other_fee'], l['month'], l['year'])
        update_database.update_remaining_dues(l['class_name'], l['month'], l['year'])
        rows = update_database.fetch_details(l['class_name'], l['month'], l['year'])
        print(rows, l['month'], l['year'])
        for row in rows :
            send_email.send_email(row, l['month'], l['year'])

    elif g.val == 2 :
        l = GUI.record_payment.payment_recorder()
        print("main", l)
        update_database.record_payment_table(l['class_name'], l['payment'], l['month'], l['year'], l['roll'])
        rows = update_database.fetch_details_of_a_student(l['class_name'], l['month'], l['year'], l['roll'])
        for row in rows :
            send_email.send_email(row, l['month'], l['year'])

    elif g.val == 3 :
        print("Nothing to do right now")
