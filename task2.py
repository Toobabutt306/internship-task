import random
import string

# Function to generate a password
def generate_password(length):
    # Define the character set (letters, digits, punctuation)
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password using the specified length
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Get user input for the desired password length
length = int(input("Enter the desired password length: "))

# Generate and display the password
password = generate_password(length)
print(f"Generated Password: {password}")
