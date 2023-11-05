import GUI.generate_fee_receipt
import GUI.record_payment
import GUI.fee_receipt_generator as g
import update_database

g.val = 3
while (g.val != 4) :
    g.input_choice()
    if g.val == 1 :
        l = GUI.generate_fee_receipt.fee_receipt_generator()
        print(l)
    elif g.val == 2 :
        l = GUI.record_payment.payment_recorder()
        print(l)
    elif g.val == 3 :
        print("Nothing to do right now")