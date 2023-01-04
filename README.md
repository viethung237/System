# System
Mô tả quá trình tạo seed :
+ sử dụng thư viện secret để tạo ra mã otp gồm 6 kí tự gồm chữ cái a -> z , A -> Z, và số
+ sử dụng OpenCv để lấy dữ liệu ảnh đầu vào
+ sử dụng sha 256 trong thư viện hashlib để băm dữ liệu ảnh và dữ liệu otp về 2 chuỗi 256 bit
+ MSB(otp) xor LSB(image)
+ ouput là chuỗi hexa 128 bit

