def clean_name(full_name):
    return full_name.strip().title()

full_name = input("Enter your full name: ")
print(clean_name(full_name))



def normalize_email(email):
    return email.strip().lower()

email = input("Enter your email: ")
print(normalize_email(email))



def is_python_file(filename):
    return filename.lower().endswith(".py")

filename = input("Enter file name: ")
print(is_python_file(filename))



def fix_message(message):
    return message.replace("bad", "good")

message = input("Enter your message: ")
result = fix_message(message)
print(result)
print(message)



def count_letter(text, letter):
    return text.lower().count(letter.lower())

text = input("Enter your text: ")
letter = input("Enter a letter: ")
print(count_letter(text, letter))



def create_login(first_name, last_name):
    first_name = first_name.strip().lower()
    last_name = last_name.strip().lower()
    return first_name + "." + last_name

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(create_login(first_name, last_name))