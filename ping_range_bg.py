import subprocess
import sys

successfully_pinged_ip = []
ping_processes = []

for i in range(1,10):
    ip_address = "192.168.1."+str(i)
    p = subprocess.Popen(["ping","-c 1",ip_address], shell=False, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    ping_processes.append((ip_address,p))

for ip,p in ping_processes:
    print(f"\033[1;33mScanning ip:{ip}\033[0m")
    stdout, stderr = p.communicate()
    if stderr:
        print(f"\033[0;31m[Error]\033[0m: says {stderr.decode('utf-8')}")
    else:
        successfully_pinged_ip.append(ip)
        print(f"\033[0;32m[Main]\033[0m Successfully pinged {ip}\n")

print(f"\n\033[1;34mSuccessfully pinged ip: \033[0m{successfully_pinged_ip}\n")