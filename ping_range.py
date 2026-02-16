import subprocess
import sys

successfully_ping_ip = []

for i in range(1,10):
    ip_address = "192.168.1."+str(i)
    print("Scanning %s"%(ip_address))
    p = subprocess.Popen(["ping","-c 1",ip_address], shell=False, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    stdout, stderr = p.communicate()
    if stderr:
        print(f"[Error] {ip_address} couldn't be pinged: says {stderr.decode('utf-8')}")
    else:
        successfully_ping_ip.append(ip_address)
        print("[Main] %s successfully pinged\n"%ip_address )

print(f"Successfully pinged ip addresses: {successfully_ping_ip}")
 