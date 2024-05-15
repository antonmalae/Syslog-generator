import socket
import string
import random
import threading
import time
from datetime import datetime
import sys
from faker import Faker

fake = Faker()

def generate_random_message():
    priority = random.randint(0, 7) 
    current_time = datetime.now().strftime("%b %d %H:%M:%S") 
    hostname = "MyComputerName" 
    words = [fake.word() for _ in range(5)] 
    message = ' '.join(words)
    log_type = random.choice(["alert", "info", "warn", "event"])
    return f"<{priority}>{current_time} {hostname} [{log_type}]: {message}"

# функция отправки сообщения
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


 # функция для отправки периодических сообщений
def send_periodic_syslog(ip, port, events_per_second):
    time_interval = 1.0 / events_per_second
    while True:
        message = generate_random_message()
        send_syslog_message(ip, port, message)
        time.sleep(time_interval)

# функция для отправки из файла
def send_from_file(ip, port, file_path):
    with open(file_path, 'r') as file:
        for line in file:
            send_syslog_message(ip, port, line.strip())
            time.sleep(1) 

def main():
    if len(sys.argv) < 4:
        print("Usage: python script.py [IP_ADDRESS] [PORT] [EVENTS_PER_SECOND] [MODE]")
        sys.exit(1)

    ip_address = sys.argv[1]
    port_number = int(sys.argv[2])
    events_per_second = float(sys.argv[3])
    mode = sys.argv[4].lower()

    if events_per_second < 1 or events_per_second > 1000:
        print("EVENTS_PER_SECOND must be between 1 and 1000")
        sys.exit(1)

    if mode == 'random':
        sys_thread = threading.Thread(target=send_periodic_syslog, args=(ip_address, port_number, events_per_second))
        sys_thread.start()
    elif mode == 'file':
        file_path = input("Enter the path to the file: ")
        send_from_file(ip_address, port_number, file_path)
    else:
        print("Invalid mode. Please use 'random' or 'file'")
        sys.exit(1)

if __name__ == "__main__":
    main()