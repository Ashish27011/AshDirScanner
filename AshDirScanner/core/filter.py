import requests
import time
def show_filter(target_url, common_url_list):

    interesting_url = 0
    filter_url_list = [ ]
    for loop in common_url_list:
     try: 
      validate = requests.get(loop, timeout=5)
      if validate.status_code not in [404, 503]:
        filter_url_list.append(loop)
        interesting_url += 1
     except requests.exceptions.ConnectionError:
      pass  
     time.sleep(0.2) 

    return filter_url_list, interesting_url
    # for p_loop in filter_url_list: 
    #   status_check = requests.get(p_loop)
    #   status_code_check =  status_check.status_code
    #   print(status_code_check)

    
