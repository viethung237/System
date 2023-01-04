import secrets
import hashlib
import cv2
import aes
# sinh ra otp gom 6 ky tu bat ki gom chu cai va so su fung thu vien secret
def generate_otp(number):
    otp_display =[]
    otp_bytes_string =''
    for i in range(number):
        num = secrets.randbelow(61)
        if(num<10):
            ch = chr(num + ord('0'))
        elif(num<36):
            ch = chr(num - 10 + ord('a'))
        else:
            ch = chr(num - 36 + ord('A'))
        otp_bytes_string += ch
        otp_display.append(ch)
    return otp_display,otp_bytes_string.encode('UTF-8')
# lay du lieu tu anh
def get_bytes_string_image(image_path):
    img = cv2.imread(image_path)
    return img.tobytes()
def resize_string_image(bytes_string_image):
    return hashlib.sha256(bytes_string_image).hexdigest()[:32].upper()
def resize_otp(otp_bytes_string):
    return hashlib.sha256(otp_bytes_string).hexdigest()[32:].upper()
#main
print("hien thi otp :",generate_otp(6)[0])
otp_bytes_string = generate_otp(6)[1]
image_bytes_string = get_bytes_string_image('lena_img.jpg')
seed = aes.xor_hex(resize_string_image(image_bytes_string),resize_otp(otp_bytes_string))
print(seed)