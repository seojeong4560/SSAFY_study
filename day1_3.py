def mask_security_number(security_number):
    num_list = list(security_number)
 
    for i in range(len(num_list) - 7, len(num_list)):
        num_list[i] = '*'
 
    return ''.join(num_list)
 
print("주민번호 입력하세요")
my_number = input()

print(mask_security_number(my_number))