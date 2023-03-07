import re
import sys

def checkPasswordStrength(password):
    pattern = re.compile(r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$")

    print('Password is Strong!') if pattern.match(password) else print('Password is weak.')

def main():
    if len(sys.argv) != 2:
        print("Please provide a password as an argument.")
        sys.exit()
    password = sys.argv[1]
    checkPasswordStrength(password)

if __name__ == '__main__':
    main()
