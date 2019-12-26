from dnschef import start_dns_server
from gad import start_cam_therad
from threading import Lock

blocked_domains = {'avi.org':'1.1.1.1'}  #TODO this should be updated from GUI,beacuse everything if passed by reference
# we can update this from any place and it will affect all apps
dns_lock = Lock()  # shared lock between cam and dns apps
dns_db = start_dns_server("127.0.0.1",blocked_urls=blocked_domains,lock_dns=dns_lock)
# dns db is the dict that both apps will use
start_cam_therad(dns_db=dns_db,dns_lock=dns_lock,blocked_urls=blocked_domains)

while True:
    pass

