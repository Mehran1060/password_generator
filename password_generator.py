import random
import string

def display_name():
    name_art = """
 __ __
| \/ |
| |\/| |
| | | |
|_| |_|
    """
    print(name_art)

def generate_password(length, use_lowercase, use_uppercase, use_digits, use_punctuation):
    characters = ""
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type must be selected")

    password = ''.join(random.choice(characters) for i in range(length))
    return password

def generate_similar_password(sample_password):
    length = len(sample_password)
    new_password = list(sample_password)
    
    # تعداد کاراکترهایی که می‌خواهیم تغییر دهیم
    num_changes = random.randint(1, max(1, length // 2))
    
    for _ in range(num_changes):
        index = random.randint(0, length - 1)
        new_char = random.choice(string.ascii_letters + string.digits + string.punctuation)
        new_password[index] = new_char
    
    return ''.join(new_password)

def get_user_input():
    try:
        length = int(input("Enter the length of the password: "))
        count = int(input("Enter the number of passwords to generate: "))
        use_lowercase = input("Include lowercase letters? (yes/no): ").strip().lower() == 'yes'
        use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
        use_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
        use_punctuation = input("Include punctuation? (yes/no): ").strip().lower() == 'yes'
        return length, count, use_lowercase, use_uppercase, use_digits, use_punctuation
    except ValueError:
        print("Please enter valid inputs.")
        return get_user_input()

def get_sample_password_input():
    try:
        sample_password = input("Enter a sample password: ")
        count = int(input("Enter the number of similar passwords to generate: "))
        return sample_password, count
    except ValueError:
        print("Please enter valid inputs.")
        return get_sample_password_input()

def save_passwords_to_file(passwords):
    filename = input("Enter the filename to save the passwords (with .txt extension): ")
    with open(filename, 'w') as file:
        for password in passwords:
            file.write(password + '\n')
    print(f"Passwords saved to {filename}")

def display_menu():
    menu = """
Select an option:
1. Generate random passwords
2. Generate similar passwords to a sample
3. Display name (M)
4. Exit
    """
    print(menu)

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            length, count, use_lowercase, use_uppercase, use_digits, use_punctuation = get_user_input()
            passwords = [generate_password(length, use_lowercase, use_uppercase, use_digits, use_punctuation) for _ in range(count)]
            
            print("\nGenerated Passwords:")
            for password in passwords:
                print(password)
            
            save = input("\nDo you want to save these passwords to a file? (yes/no): ").strip().lower()
            if save == 'yes':
                save_passwords_to_file(passwords)
            else:
                print("Passwords were not saved.")
        
        elif choice == '2':
            sample_password, count = get_sample_password_input()
            passwords = [generate_similar_password(sample_password) for _ in range(count)]
            
            print("\nGenerated Similar Passwords:")
            for password in passwords:
                print(password)
            
            save = input("\nDo you want to save these passwords to a file? (yes/no): ").strip().lower()
            if save == 'yes':
                save_passwords_to_file(passwords)
            else:
                print("Passwords were not saved.")
        
        elif choice == '3':
            display_name()
        
        elif choice == '4':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()