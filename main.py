from datetime import datetime
import re
with open("sample_logs.txt", "r") as file:  
    linecount = 0
    bruteForce = 0
    failedIP = {

    }
    eventTracker ={

    }
    for line in file:
        linecount+=1
        line = line.strip()
        match = re.search(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", line)
        ip = re.search(r"\d+\.\d+\.\d+\.\d+", line)


        if(linecount>1):
            oldTime = newTime
            newTime = datetime.strptime(match.group(), "%Y-%m-%d %H:%M:%S")
            timeDifference = newTime - oldTime
        else:
            newTime = datetime.strptime(match.group(), "%Y-%m-%d %H:%M:%S")
        

        words = line.split()

        event = words[2]
        if event not in eventTracker:
            eventTracker[event] = 1
        else:
            eventTracker[event] += 1

        for word in words:
            if(event == "LOGIN_FAILED"):
                if ip.group() not in failedIP:
                    failedIP[ip.group()] = 1
                else:
                    failedIP[ip.group()] += 1
                if(failedIP[ip.group()])==3:
                     bruteForce += 1
    
    topIP = max(failedIP, key=failedIP.get)
    totalFailed = eventTracker.get("LOGIN_FAILED", 0)

    with open("report.txt", "w") as report:
        
        report.write("=== Security REPORT ===\n\n")
        
        report.write(f"REPORT GENERATED AT: {datetime.now()}\n")

        report.write("\n== EVENT SUMMARY ==\n\n")
        for event, count in eventTracker.items():
            report.write(f"{event:<18} | Count: {count}\n")

        report.write("\n== ATTACK LOGS ==\n")
        report.write(f"\nBRUTE FORCE ALERTS: {bruteForce}\n")

        report.write("SEVERITY LEVEL: ")
        if(totalFailed < 6):
            report.write("Low")
        elif(totalFailed < 10):
            report.write("Medium")
        else:
            report.write("HIGH")

        report.write(f"\nATTACK TYPES DETECTED:")
        if(bruteForce>0):
            report.write("BruteForce \n")
            report.write("Reason: IPS:")
            for ip in failedIP:
                if failedIP[ip] > 2:
                    report.write(ip + " ")
            report.write("\nhad several failed login attempts in a short period of time.")
        else:
            report.write("NONE")


        report.write("\n\n== Suspicious IPS==\n\n")


        for ip in failedIP:
            report.write(f"{ip:<18} | Failed Attempts: {failedIP[ip]:<3}\n")

        report.write("\n=== RECOMMENDED ACTION ===\n\n")
        if(totalFailed < 6):
            report.write("No large action needed, keep monitoring system accordnigly.\n")
        elif(totalFailed < 10):
            report.write("-Check failed login attempts \n -Check IP addresses with multiple failed attempts.\n")
        else:
            report.write("- Investigate repeated failed logins immediately.\n")
            report.write("- Consider temporarily blocking high-risk IPs.\n")
            report.write("- Review account activity for compromise.\n")


                
            


