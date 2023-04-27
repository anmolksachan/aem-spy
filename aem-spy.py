import argparse
import requests

BANNER = """
   ___   ______  ___  _________  __
  / _ | / __/  |/  / / __/ _ \ \/ /
 / __ |/ _// /|_/ / _\ \/ ___/\  /
/_/ |_/___/_/  /_/ /___/_/    /_/
     by @FR13ND0x7F
"""

def check_aem(url):
    try:
        response = requests.get(url)
        if "adobedtm" in response.text:
            print(f"[+] Possible AEM detected for {url}")
        else:
             print(f"[-] Checking {url}")
    except:
        print(f"Error checking {url}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check a list of URLs for possible AEM detection")
    parser.add_argument("--target", dest="target_file", required=True, help="Path to file containing URLs")
    args = parser.parse_args()

    print(BANNER)
    with open(args.target_file, "r") as f:
        urls = f.read().splitlines()

    for url in urls:
        check_aem(url)
