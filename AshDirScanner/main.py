from banners import banner
from core import validator
from core import wordlist
from core import scanner
from core import reporter
from core import filter
from outputs import writeups

target_url = validator.show_validator()
banner.s_banner()
print("")
common_url_list, total_tested = wordlist.show_wordlist(target_url)
filter_url_list, interesting_url =  filter.show_filter(target_url, common_url_list)
status_code_list, server_list, content_length_list, content_Type_list = scanner.show_scanner(filter_url_list)
reporter.show_reports(target_url, total_tested, filter_url_list, interesting_url, status_code_list, server_list, content_length_list, content_Type_list)
writeups.show_writeup(target_url, total_tested, filter_url_list, interesting_url, status_code_list, server_list, content_length_list, content_Type_list)
print("")
print("Report Saved Successfully in [report.txt]")
print("")
banner.e_banner()