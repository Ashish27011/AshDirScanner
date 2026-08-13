from urllib.parse import urlparse
import requests
def show_validator():
    while True:
        try:
            target_url = input("Enter URL :")
            url_check = urlparse(target_url)
            check_host = url_check.hostname
            
            if url_check.scheme not in ["http", "https"]:
                print("Invalid scheme! Use http or https")
                continue
                
            if not check_host:
                print("Invalid URL! Missing domain")
                continue
                
            else:
                break
                
        except:
            print("Enter Valid URL!")
            continue
    return target_url     