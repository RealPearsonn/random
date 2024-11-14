import requests
import string
import random
from time import sleep

def check_username(username):
    url = f'https://www.roblox.com/SignUp/UsernameAvailability?username={username}'
    response = requests.get(url)
    
    # Check if the response indicates the username is available
    if response.status_code == 200:
        if "isAvailable" in response.text and '"isAvailable":true' in response.text:
            return True
    return False

def generate_username():
    # Generate a random 4-letter username
    return ''.join(random.choices(string.ascii_lowercase, k=4))

def find_available_username():
    while True:
        username = generate_username()
        print(f"Checking username: {username}")
        
        if check_username(username):
            print(f"Found available username: {username}")
            return username
        else:
            print(f"Username {username} is taken.")
        
        # Add a small delay to avoid overwhelming Roblox's servers
        sleep(1)

if __name__ == "__main__":
    print("Starting search for an available 4-letter Roblox username...")
    available_username = find_available_username()
    print(f"Available username found: {available_username}")
