shift=int(input())
message=input()
decode=""
for char in message:
    if char.isalpha():
        is_upper=char.isupper()
        char_code=ord(char)-shift
        if is_upper:
            if char_code<ord('A'):
                char_code+=26
        else:
            if char_code<ord('a'):
                char_code+=26
        decode+=chr(char_code)
    else:
        decode+=char
print(decode)