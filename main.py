from datetime import datetime
import re
with open("sample_logs.txt", "r") as file:
    failedCount = 0  
    linecount = 0
    failedIP = {

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
            if(timeDifference.total_seconds()>= 10):
                failedCount = 0
        else:
            newTime = datetime.strptime(match.group(), "%Y-%m-%d %H:%M:%S")
        

        words = line.split()
        for word in words:
            if(word == "LOGIN_FAILED"):
                failedCount += 1
                print("LOGIN FAIL")
                print("Current Count", failedCount)
                if ip.group() not in failedIP:
                    failedIP[ip.group()] = 1
                else:
                    failedIP[ip.group()] += 1
                    print(failedIP[ip.group()])

                if (failedCount > 2):
                    print("Suspicous Activity Detected")


                
            


