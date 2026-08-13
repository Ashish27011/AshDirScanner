def show_wordlist(target_url):
    total_tested = 0
    common_url_list = [ ]
    file_check = open('AshDirScanner/worldlists/common.txt', "r")
    for word_list in file_check:
        com_url = target_url +'/'+ word_list.strip()  
        common_url_list.append(com_url)
        total_tested += 1
    return common_url_list, total_tested          