import smtplib
User_mail = input("E mail : ")
User_password = input("Password : ")
with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(User_mail, User_password)
    Subject = input("Type your subject :")
    Body = input("Type your message :")

    msg = f"Subject : {Subject} \n\n {Body}"
    Reciever_mail = input("Enter receivers mail :")
    smtp.sendmail(User_mail,Reciever_mail,msg)