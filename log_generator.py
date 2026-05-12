from datetime import datetime
import time, random

with open("sample_logs.txt", "w") as file:
    events = ["LOGIN_SUCCESS", "LOGIN_FAILED", "ACCOUNT_LOCKED", "UNKNOWN_USER"]
    attacks = ["Brute_Force", "Normal_Activity", "Normal_Activity"]
    users = ["admin","frank","sohum"]
    for i in range(random.randint(3,10)):
        if(attacks[random.randint(0,2)] == "Brute_Force"):
            ip = f"{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"
            for i in range(random.randint(3,7)):
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"{timestamp} LOGIN_FAILED {ip}\n")
        else:
            ip = f"{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{timestamp} {events[random.randint(0,len(events)-1)]} {ip}\n")
        time.sleep(.25)