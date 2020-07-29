port1 = {21: "FTP", 22:"SSH", 23: "telnet", 80:"http"}
port2 = dict([(value, key) for key, value in port1.items()]) 
print ("port1:") 
print(port1)  
print ("port2:")
print(port2)
