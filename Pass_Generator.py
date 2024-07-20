import random


class Password_generator():

    def create_password(self):

        letters = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
            'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        ]
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        nr_letters = random.randint(3, 7)
        nr_symbols = random.randint(3, 7)
        nr_numbers = random.randint(3, 7)

        letters_pass = ""
        for n in range(0, nr_letters):
            random_letter = random.randint(0, len(letters) - 1)
            letters_pass += letters[random_letter]
        symbols_pass = ""
        for n in range(0, nr_symbols):
            random_symbol = random.randint(0, len(symbols) - 1)
            symbols_pass += symbols[random_symbol]
        numbers_pass = ""
        for n in range(0, nr_numbers):
            random_number = random.randint(0, len(numbers) - 1)
            numbers_pass += numbers[random_number]
        password_list = list(letters_pass + symbols_pass + numbers_pass)
        random.shuffle(password_list)
        password = "".join(password_list)
        return password


