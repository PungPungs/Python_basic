import socket
import subprocess
import time

def is_connected():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        return False

def disable_network(interface_name="이더넷"):
    subprocess.run(f'netsh interface set interface "{interface_name}" admin=disable', shell=True)

def monitor_and_block():
    while True:
        if is_connected():
            print("인터넷 연결됨. 차단 중...")
            disable_network()
            continue
        else:
            print("인터넷 연결 안 됨. 감시 중...")
        time.sleep(5)

if __name__ == "__main__":
    monitor_and_block()
