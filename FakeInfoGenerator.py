from faker import Faker
fake = Faker()

print("""        
  __  __                _  _
 |  \/  |              | |/ /                 | |        
 | \  / |  _ __        | ' /    __ _   _   _  | |   ___  
 | |\/| | | '__|       |  <    / _` | | | | | | |  / _ \ 
 | |  | | | |     _    | . \  | (_| | | |_| | | | | (_) |
 |_|  |_| |_|    (_)   |_|\_\  \__,_|  \__, | |_|  \___/ 
                                        __/ |            
                                       |___/
      
  ______           _               _____            __              _____                                        _                  
 |  ____|         | |             |_   _|          / _|            / ____|                                      | |                 
 | |__      __ _  | | __   ___      | |    _ __   | |_    ___     | |  __    ___   _ __     ___   _ __    __ _  | |_    ___    _ __ 
 |  __|    / _` | | |/ /  / _ \     | |   | '_ \  |  _|  / _ \    | | |_ |  / _ \ | '_ \   / _ \ | '__|  / _` | | __|  / _ \  | '__|
 | |      | (_| | |   <  |  __/    _| |_  | | | | | |   | (_) |   | |__| | |  __/ | | | | |  __/ | |    | (_| | | |_  | (_) | | |   
 |_|       \__,_| |_|\_\  \___|   |_____| |_| |_| |_|    \___/     \_____|  \___| |_| |_|  \___| |_|     \__,_|  \__|  \___/  |_|""")
print("____________________________")
print("<1> Full name")
print("<2> Email")
print("<3> Password")
print("<4> Phone number")
print("<5> Address")
print("<6> Country")
print("<7> Ipv4")
print("<8> Ipv6")
print("<9> Date of birth")
print("<10> Fake id")
print("<99> Exit")
print("____________________________")

q = int(input("Choice:\n"))

if q == 1:    
    num = int(input("How many full names do you want?\n"))
    for i in range(num):
        print(fake.name())

elif q == 2:
    num1 = int(input("How many emails do you want?\n"))
    for i in range(num1):
        print(fake.free_email())

elif q == 3:
    num2 = int(input("How many passwords do you want?\n"))
    for i in range(num2):
        print(fake.password())

elif q==4:
    num3 = int(input("How many phone numbers do you want?\n"))
    for i in range(num3):
        print(fake.phone_number())

elif q==5:
    num4 = int(input("How many addresses?\n"))
    for i in range(num4):
        print(fake.address())

elif q==6:
    num5 = int(input("How many countries?\n"))
    for i in range(num5):
        print(fake.country())

elif q==7:
    num6 = int(input("How many Ipv4?\n"))
    for i in range(num6):
        print(fake.ipv4())

elif q==8:
    num7 = int(input("How many Ipv6?\n"))
    for i in range(num7):
        print(fake.ipv6())

elif q==9:
    num8 = int(input("How many Date of birth?\n"))
    for i in range(num8):
        print(fake.date_of_birth())

elif q==10:
    num9 = int(input("How many fake ids?\n"))
    for i in range(num9):
        print("______________________________________________________________")
        print("Full name: "+fake.name())
        print("Email: "+fake.free_email())
        print("Password: "+fake.password())
        print("Phone number: "+fake.phone_number())
        print("Date of brith: "+fake.date_of_birth().strftime("%Y-%m-%d"))
        print("Address: "+fake.address())
        print("Ipv4: "+fake.ipv4())
        print("Ipv6: "+fake.ipv6())
        print("______________________________________________________________")


elif q==99:
    i = 0
    while False:
        print(i)
        i +=1
        if i == 0:
            break

else:
    print("Invalid choice")

print("""______________________________________________________________
      Buy use a coffee<:
bitcoin:bc1qrh7r2zupwdw929pj77eugww5vhncjyrh9tx846
usdt:0x9413AAF1CC5A53EFF1177d5b7D509B0AEEC154BA
bitcoincash:qrcgr35p7cpnepyjayqdka64ng57c4ag3ykc7jh7yk
litecoin:ltc1qus4k3mttp66p2vqr8ln7rp69hnndg7qpr5ls3a
ethereum:0x9413AAF1CC5A53EFF1177d5b7D509B0AEEC154BA
ton:UQDcPWbI6fPCTyqHXK73iWT5YUAoC3Slx9yHmrfgrL07Er1i
dash:XoP7HyBGG97HM367ihJgKCPYmuLTCEdLwD
bnb:0x9413AAF1CC5A53EFF1177d5b7D509B0AEEC154BA
trx:TUkpoTqwWvrqxZjEMF61Kx2oqXGLViaGsS
______________________________________________________________""")