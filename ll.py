def filter_usernames(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        usernames = infile.readlines()
        usernames = [username.strip() for username in usernames if len(username.strip()) == 4]
        outfile.write('\n'.join(usernames))

if __name__ == "__main__":
    input_filename = "input.txt"  # Replace this with the name of your input file
    output_filename = "username.txt"

    filter_usernames(input_filename, output_filename)
