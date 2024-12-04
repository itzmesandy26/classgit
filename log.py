import datetime

def division(dividend, divisor):
    
    try:
        result = dividend / divisor
        status = "No error"
    except Exception as e:
        result = f"ERROR OCCURED : {e}"
        status = "Error encountered !"
    finally:
        final = "CODE EXECUTED SUCCESSFULLY"
 
    date = datetime.datetime.now().strftime(" %d - %m - %Y ")
    time = datetime.datetime.now().strftime(" %H : %M : %S ")

    log_entry = f"DATA : {date} TIME : {time}, DIVIDEND : {dividend}, DIVISOR : {divisor}, RESULT : {result}, STATUS : {status}, {final} \n\n"
    
    with open("DATA", "a") as file:
        file.write(log_entry)

while True:
    dividend = float(input("Enter the DIVIDEND : "))
    divisor = float(input("Enter the DIVISOR : "))
    division(dividend, divisor)