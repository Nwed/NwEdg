import random
import string

def generate_username(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def main():
    num_usernames = 10000  # You can change this number as needed
    username_length = 4
    usernames = [generate_username(username_length) for _ in range(num_usernames)]

    with open("username.txt", "w") as f:
        for username in usernames:
            f.write(username + "\n")

    print(f"{num_usernames} usernames generated and saved to username.txt")

if __name__ == "__main__":
    main()
