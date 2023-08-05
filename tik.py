def check_usernames(username_list):
    for username in username_list:
        if is_taken(username):
            print(f"The username '{username}' is taken.")
        else:
            print(f"The username '{username}' is available.")

def is_taken(username):
    # Add your logic here to check if the username is taken or not
    # You can use APIs, databases, or any other method to perform the check
    # For demonstration purposes, let's assume the username is taken if it starts with 'admin'
    return username.startswith('admin')

# Prompt the user for the filename containing the list of usernames
filename = input("Enter the name of the file containing the usernames: ")

try:
    with open(filename, 'r') as file:
        usernames = file.read().splitlines()
        check_usernames(usernames)
except FileNotFoundError:
    print(f"File '{filename}' not found.")

