import requests

def validate_url(VALIDATOR_PUBLIC_KEY):
  
  url = f'https://xrpscan.com/validator/{VALIDATOR_PUBLIC_KEY}'
  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for non-2xx status codes
    return response.status_code
  except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
    return -1
  except ValueError:
    print("Invalid XRP address format.")
    return -1
# Get user input for the wallet address
public_key = input("Enter your XRP public key: ")

# Validate the address and check the URL status
status_code = validate_url(public_key)

if status_code == 200:
  print("URL is functioning correctly!")
elif status_code == -1:
  # Address validation error or other error
  pass
else:
  print(f"Error: Status code {status_code}")
