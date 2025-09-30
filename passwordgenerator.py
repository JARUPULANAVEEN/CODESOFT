import random
import string

# Password Generator
print("------ Password Generator ------")

# Step 1: User input for password length
length = int(input("Enter desired password length: "))

# Step 2: Define possible characters (letters, digits, symbols)
characters = string.ascii_letters + string.digits + string.punctuation

# Step 3: Generate password
password = ''.join(random.choice(characters) for _ in range(length))

# Step 4: Display password
print("Generated Password:", password)
