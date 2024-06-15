import random

alpha = 'abcdefghijklmnopqrstuvwxyz1234567890'


def encoded_msg():
    user_message = input("Enter the message: ")

    if ' ' not in user_message:
        print(''.join(random.sample(alpha,3)) + user_message.replace(user_message[0],'') + user_message[0] + ''.join(random.sample(alpha,3)))

    else:
        cap_msg = user_message.title()
        no_space_msg = cap_msg.replace(' ','')
        print(' ' + ''.join(random.sample(alpha,3)).upper() + no_space_msg[::-1] + ''.join(random.sample(alpha,3)).upper())
   
def decoded_msg():
    user_message = input("Enter the message: ")

    if ' ' not in user_message:
        print(user_message[len(user_message)-4] + user_message[3:len(user_message)-4])
    
    elif ' ' in user_message:
        decoded_message = user_message[4:len(user_message)-3][::-1]
        print(decoded_message)

while True: 
    code_decode = input("Enter 1 to encode, 2 to decode, or 3 to exit:")
    if code_decode=='1':
        encoded_msg()
    elif code_decode=='2':
        decoded_msg()
    elif code_decode=='3':
        print("Exiting the program!")
        break
    else:
        print("Invalid input!\nEnter 1,2 or 3.")
        pass