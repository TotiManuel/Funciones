from email.message import EmailMessage
import smtplib
remitente = "manuel.mandaio@gmail.com"
destinatario = "manuel.mandaio@gmail.com"
contrasena="fpnyepcjkfrvhklh"
mensaje = "¡Hola, mundo!, Mensaje Enviado"
email = EmailMessage()
email["From"] = remitente
email["To"] = destinatario
email["Subject"] = "Correo de prueba"
email.set_content(mensaje)
smtp = smtplib.SMTP_SSL("smtp.gmail.com")
smtp.login(remitente, contrasena)
smtp.sendmail(remitente, destinatario, email.as_string())
smtp.quit()