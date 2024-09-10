import re
import math

def passwdd_strenth_checker(passwd):
    quotes = []
    len_pass = len(passwd)

    # checking for length of password
    if len_pass < 12:
        quotes.append("-> Password length should be at least 12 characters.")

    # checking for uppercase letters
    if not re.search(r'[A-Z]', passwd):
        quotes.append("-> Add at least one [A-Z] Uppercase character")

    # checking for lowercase letters
    if not re.search(r'[a-z]', passwd):
        quotes.append("-> Add at least [a-z] one lowercase character")

    # checking for
    if not re.search(r'[0-9]', passwd):
        quotes.append("-> Add at least one [0-9] numerical character")

    if not re.search(r'[!@#$&*()_{}<>.,~`]', passwd):
        quotes.append("-> Add at least one [!@#$&*()_{}<>.,~`] special character")

    if not quotes:
        print("-> Strong password!")
    else:
        for i in quotes:
            print(i)

    password_entropy(passwd, len_pass)

#Checking for password complexity
def password_entropy(passwd, len_pass):
    character_set = 0

    if re.search(r'[A-Z]', passwd):
        character_set += 26
    if re.search(r'[a-z]', passwd):
        character_set += 26
    if re.search(r'[0-9]', passwd):
        character_set += 10
    if re.search(r'[!@#$&*()_{}<>.,~`]', passwd):
        character_set += 17

    entropy = math.log2(character_set**len_pass)
    if entropy > 128:
        print("-> Password complexity is: Very Strong")
    elif entropy >= 60 and entropy <= 127:
        print("-> Password complexity is: Strong")
    elif entropy >= 36 and entropy <= 59:
        print("-> Password complexity is: Moderate")
    elif entropy >= 28 and entropy <= 35:
        print("-> Password complexity is: Weak")
    elif entropy <= 28:
        print("-> Password complexity is: Very Weak")
    else:
        pass

    time_in_seconds = time_to_crack(len_pass, character_set)
    years, days, hours, minutes, seconds = convert_time(time_in_seconds)

    print(f"-> password Entropy: {entropy:.2f} bits")
    print("-> Estimated time to crack the password by brute force with high performance machine:")
    print(f"-> {years} years, {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")

def time_to_crack(len_pass, character_set):
    total_combinations = character_set ** len_pass
    time_in_seconds = total_combinations / 10**9
    return time_in_seconds


def convert_time(seconds):
    minute = 60
    hour = 60 * minute
    day = 24 * hour
    year = 365 * day

    years = seconds // year
    seconds %= year
    days = seconds // day
    seconds %= day
    hours = seconds // hour
    seconds %= hour
    minutes = seconds // minute
    seconds %= minute

    return int(years), int(days), int(hours), int(minutes), int(seconds)

def uniqueness(passwd):
    with open('common_passwords.txt', "r") as file:
        file_passwords = file.read()
        list_passwords = file_passwords.split()
        if passwd in list_passwords:
            print(f"-> {passwd} is common password. Please enter a unique password.")

if __name__ == '__main__':
    password = input("please enter a password to check strength: \n")
    passwdd_strenth_checker(password)
    uniqueness(password)
