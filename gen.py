import socket
import random
import string
import threading
import time
from datetime import datetime
import sys

def generate_random_message():
    priority = random.randint(0, 7) 
    current_time = datetime.now().strftime("%b %d %H:%M:%S") 
    hostname = "MyComputerName" 
    message = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
    log_type = random.choice(["alert", "info", "warn", "event"])
    return f"<{priority}>{current_time} {hostname} [{log_type}]: {message}"

def send_syslog_message(ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (ip, port)
    
    try:
        sock.sendto(message.encode(), server_address)
        print(f"Syslog message sent to {ip}:{port}: {message}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        sock.close()

def send_periodic_syslog(ip, port):
    while True:
        message = generate_random_message()
        send_syslog_message(ip, port, message)
        time.sleep(0.2)  

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py [IP_ADDRESS] [PORT]")
        sys.exit(1)

    ip_address = sys.argv[1]
    port_number = int(sys.argv[2])

    sys_thread = threading.Thread(target=send_periodic_syslog, args=(ip_address, port_number))
    sys_thread.start()
