
import hashlib
import cv2
import aes
# sinh ra otp gom 6 ky tu bat ki gom chu cai va so su fung thu vien secret
def generate_otp(num):
    if (num < 10):
        ch = chr(num + ord('0'))
    elif (num < 36):
        ch = chr(num - 10 + ord('a'))
    else:
        ch = chr(num - 36 + ord('A'))
    return ch
# lay du lieu tu anh
def get_bytes_string_image(image_path):
    img = cv2.imread(image_path)
    return img.tobytes()
def sha_resize(bytes_string):
    return hashlib.sha256(bytes_string).hexdigest()[:60].upper()
def otp(image_hex_string):
    split = []
    for i in range(0, len(image_hex_string), 10):
        split.append(int(aes.hex_to_bin(image_hex_string[i:i + 10])) % 62)
    otp = []
    for i in split:
        otp.append(generate_otp(int(i)))
    return otp
#main
image_bytes_string = get_bytes_string_image('lena_img.jpg')
image_hex_string = sha_resize(image_bytes_string)
test_bytes_string = get_bytes_string_image('modified.jpg')
test_hex_string = sha_resize(test_bytes_string)
print(otp(image_hex_string))
print(otp(test_hex_string))






