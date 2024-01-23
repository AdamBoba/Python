import threading
import time

def watek1():
    while True:
        print("test")
        time.sleep(5)

def watek2():
    while True:
        print("test1")
        time.sleep(1)

if __name__ == "__main__":
    
    thread1 = threading.Thread(target=watek1)
    thread2 = threading.Thread(target=watek2)

    
    thread1.start()
    thread2.start()

    try:
        
        while True:
            pass
    except KeyboardInterrupt:
        
        print("Przerwano program.")

    
    thread1.join()
    thread2.join()
