import random
import string

def generate_password(length,complexity):
    if complexity == 'weak':
        char_sets = string.ascii_lowercase + string.digits
    elif complexity == 'strong':
        char_sets = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    else:
        print("Complexity must be either strong or weak")
    password = ''.join(random.choice(char_sets) for _ in range(length))
    return password

def main():
    length = int(input("Enter the length of the password : "))
    complexity = input("Enter the complexity (weak/strong) : ").lower()
    password = generate_password(length,complexity)
    print(f'Generated password: {password}')
if __name__ == "__main__":
    main()
