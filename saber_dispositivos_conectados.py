#antes descargar la libreria con el comando:
# pip install python-nmap
import nmap

scanner = nmap.PortScanner()
ip = input("Direccion IP: [192.168.0.0/24]")
scanner.scan(ip)

print(scanner.all_hosts())
