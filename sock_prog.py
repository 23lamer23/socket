import socket

ports = [[80,'http'],[443,'ssl'],[22,'ssh'],[445,'smb'],[20,'ftp'],[21,'ftp'],[23,'telnet'],[3306,'mysql'],[53,'dns'],[67,'dhcp'],[68,'dhcp'],[88,'kerberos'],[3389,"remote desktop"]]

#port taraması için fonksiyon
server = input("hedef ip adresini giriniz: ")
def portscanner(port,server):
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        soc.connect((server,port[0]))
        return f'\nhedef sistemin {port[0]} numaralı {port[1]} portu açık.'
        soc.close()
    except:
        soc.close()
        pass
    else:
        pass
#portların taranması
for i in ports:
    result = portscanner(i,server)
    if result != None:
        print(result)
