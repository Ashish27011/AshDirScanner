def show_writeup(target_url, total_tested, filter_url_list, interesting_url, status_code_list, server_list, content_length_list, content_Type_list):

    file = open('AshDirScanner/reports/report.txt', "w")
    file.write("\n")
    file.write(f"{"Target : "} + str{target_url}\n")
    file.write("\n")
    file.write(f"{'STATUS':<8} {'server':<20} {'LENGTH':<10} {'TYPE':<40} {'PATH':<60}\n")
    file.write("-" * 160 + "\n")

    for status, server, lenght, type, path in zip(status_code_list, server_list, content_length_list, content_Type_list, filter_url_list):
        file.write(f"{status:<8} {server:<20} {lenght:<10} {type:<40} {path:<60}\n")   

    file.write("-"*160)
    file.write("\n")
    file.write(f"{"Tested : "} + str{total_tested}\n")
    file.write(f"{"Interesting : "} + str{interesting_url}\n")      
    file.close() 