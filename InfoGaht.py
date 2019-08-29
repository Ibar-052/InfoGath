#python3
import os, sys

os.system("clear")
print("""
╔══╗╔═╦╗╔══╗╔═╗╔══╗╔╗╔╗╔══╗╔══╗
╚║║╝║║║║║═╦╝║║║║╔═╣║╚╝║║╔╗║╚╗╔╝
╔║║╗║║║║║╔╝─║║║║╚╗║║╔╗║║╠╣║─║║─
╚══╝╚╩═╝╚╝──╚═╝╚══╝╚╝╚╝╚╝╚╝─╚╝─
""")
nama = input("masukkan nama pengguna : ")
#keluar
def keluar():
    mmk = input("lanjut [y/t] --> ")
    if mmk == 't' or mmk == 'T':
       exit()
    else:
       if mmk == 'y' or mmk == 'Y':
          os.system("clear")
          print(banner)
          print("USER : ",nama)
          print(menu)
          print(pilihan())
       
os.system("clear")
#banner
banner = ("""
    ╔╗╴╴╴╔══════╗ Author = Ibar052
    ║║╴╴╴║╴╔════╝ Code   = Python3
    ║╚═══╝╴╚════╗ Team   = 407 Authentic Exploit
    ╚════╗╴╔═══╗║
    ╔════╝╴║╴╴╴║║
    ╚══════╝╴╴╴╚╝
""")

#menu
menu = ("""
    {1}. Reverse Ip Lookup
    {2}. DNS Lookup
    {3}. GeoIP Lookup
    {4}. Whois Lookup
    {5}. Traceroute
    {6}. Reverse DNS Lookup
    {7}. Port Scan
    {8}. Exit
""")

print(banner)
print("USER : ", nama)
print(menu)

#input
def pilihan():
    kntl = input("pilih nomer~> ")
    if kntl == '1':
       cok = input("Masukkan Ip Atau Domain : ")
       os.system("curl http://api.hackertarget.com/reverseiplookup/?q="+cok)
       print("")
       print("")
       keluar()
    elif kntl == '2':
       cok = input("Masukkan Domain : ")
       os.system("curl http://api.hackertarget.com/dnslookup/?q="+cok)
       print("")
       print("")
       keluar()
    elif kntl == '3':
       cok = input("Masukkan Ip : ")
       os.system("curl http://api.hackertarget.com/geoip/?q="+cok)
       print("")
       print("")
       keluar()
    elif kntl == '4':
       cok = input("Masukkan Ip Atau Domain : ")
       os.system("curl http://api.hackertarget.com/whois/?q="+cok)
       print("")
       print("")
       keluar()
    elif kntl == '5':
       cok = input("Masukkan Ip Atau Domain : ")
       os.system("curl https://api.hackertarget.com/mtr/?q="+cok)
       print("")
       print("")
       keluar()
    elif kntl == '6':
       cok = input("Masukkan Ip - Rentang Ip Atau Domain : ")
       os.system("curl https://api.hackertarget.com/reversedns/?q="+cok)
       print("")
       print("")
       keluar()
    elif kntl == '7':
       cok = input("Masukkan Ip Atau Domain : ")
       os.system("curl http://api.hackertarget.com/nmap/?q="+cok)
       print("")
       print("")
       keluar()
       
if __name__ == "__main__":
     while(True):
         pilihan()
     