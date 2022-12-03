import morse_dict
run = True

while run:
    output = input('Type your message text here or hit * to end: ').lower()
    answer = list(output)
    morse_message = []

    for letter in answer:
        morse_message.append(morse_dict.morse_code_dictionary[letter])

    morse_message = ''.join(morse_message)

    if morse_message == '*':
        run = False
    else:
        print(f'\n{morse_message}\n\n')



