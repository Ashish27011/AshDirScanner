import requests
import time
def show_scanner(filter_url_list): 
   status_code_list = []
   server_list = []
   content_length_list = []
   content_Type_list = []

   for request_loop in filter_url_list:  

    try:
      request_loop = request_loop.strip()           
      valid_request = requests.get(request_loop, timeout=5)
      Status_code = valid_request.status_code
      server = valid_request.headers.get("server", "N/A")
      content_length = valid_request.headers.get("Content-length", "N/A")
      content_Type = valid_request.headers.get("Content-Type", "N/A")
      status_code_list.append(Status_code)
      server_list.append(server)
      content_Type_list.append(content_Type)
      content_length_list.append(content_length)
    except requests.exceptions.ConnectionError:
      pass
    time.sleep(0.2) 

   return status_code_list, server_list, content_length_list, content_Type_list
     