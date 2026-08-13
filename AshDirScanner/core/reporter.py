def show_reports(target_url, total_tested, filter_url_list, interesting_url, status_code_list, server_list, content_length_list, content_Type_list):
    print("")
    print("Target : ", target_url)
    print("")
    print(f"{'STATUS':<8} {'server':<20} {'LENGTH':<10} {'TYPE':<40} {'PATH':<60}")
    print("-" * 160)
    for status, server, lenght, type, path in zip(status_code_list, server_list, content_length_list, content_Type_list, filter_url_list):
        print(f"{status:<8} {server:<20} {lenght:<10} {type:<40} {path:<60}")
    print("-"*160)
    print("")
    print("Tested : ", total_tested)
    print("Interesting : ", interesting_url)    
