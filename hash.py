

class Hash():
    def __init__(self):
        self.carac_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
    'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
    'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
    'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '_'] 



    def crypt_password(self,password,key):
        pass_crypt = "#1"
        for i in range(len(password)):
            ch = password[i]
            ch2 = key[i]
            #ch doit donner ça valeur ASCII (exemple r = 114) et etre diviser par 16
            num2 = int(ord(ch) / 16)
            num3 = int(ord(ch) % 16)
            index = int((num2 + ord(ch2)) % len(self.carac_array))
            num5 = int((num3 + ord(ch2)) % len(self.carac_array))
            
            pass_crypt = pass_crypt + self.carac_array[index] + self.carac_array[num5]
        return str(pass_crypt)


         
    def decrypt_IP(self,packet):
        ip = ""
        for i in range(0,8,2):
            frist = int(ord(packet[i])  - 48) 
            segond = int(ord(packet[i+1]) - 48) 
            
            if i != 0:
                ip += (".")

            ip += str((((frist & 15) << 4) | (segond & 15)))
        return str(ip)


if __name__ == "__main__":
    ca = Hash()
    ca.decrypt_IP(":<41=214")