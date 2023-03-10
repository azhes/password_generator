import random
import string

def import_words(filename):
    words = []
    with open(filename, 'r') as f:
        for line in f:
            words.append(line.strip())

    return words

def user_pass_gen(words):
    pw_word = random.choice(words)
    while len(pw_word) < 5:
        pw_word = random.choice(words)
    pw_word = pw_word.capitalize()
    pw_num = random.randint(100, 1000)
    pw_symbol = random.choice(string.punctuation)

    password = f'{pw_word}{pw_symbol}{pw_num}'

    return password

def secure_pass_gen():
    password = ''
    characters = string.ascii_letters + string.digits + string.punctuation
    pw_length = random.randint(15, 20)
    for i in range(pw_length):
        character = random.choice(characters)
        if character != "\n" and character != "\r" and character != "\t" and character != '' and character != '\x0b' and character != '\x0b':
            password += character

    return password

def gen_passwd():
    valid_temp = ['temporary', 'temp', 'temporary user', 'temporary user password', 'temporary password', 't', 'u', 'user']
    valid_secure = ['secure', 'sec', 'secure password', 's']

    password_type = input(f'Would you like to generate a temporary user password or a secure password? ')
    while password_type not in valid_temp and password_type not in valid_secure:
            print(f'\nValid arguments:\n')
            print(f'Temporary password:')
            print(f'------------------')
            for arg in valid_temp:
                print(arg)
            print(f'\nSecure password:')
            print(f'---------------')
            for arg in valid_secure:
                print(arg)
            password_type = input(f'Please enter a valid argument: ')

    if password_type in valid_temp:
        words = import_words("words.txt")
        password = user_pass_gen(words)
    elif password_type in valid_secure:
        password = secure_pass_gen()

    print(password)

    response = input(f'Would you like to generate another password (y/n)? ')

    valid_yes = ['yes', 'y', 'Yes', 'Y', 'Yep', 'yep']
    valid_no = ['no', 'n', 'No', 'N', 'nah', 'Nah']

    while response not in valid_no and response not in valid_yes:
        response = input(f'Please type "yes" or "no". ')

    if response in valid_yes:
        kg = True
    elif response in valid_no:
        kg = False

    return kg

def main():
    kg = True
    while kg ==True:
        kg = gen_passwd()

    print(f'Thank you for using my password generator :)')

if __name__ == "__main__":
    main()