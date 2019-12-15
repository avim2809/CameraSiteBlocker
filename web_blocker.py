#host_path= r"C:\Windows\System32\drivers\etc\hosts"
host_path = "hosts"
redirect = "127.0.0.1"
website_list = ["facebook.com","www.facebook.com"]

def block_host():
    with open(host_path,'r+') as file:
        content = file.read()
        for website in website_list:
            if website in content:
                pass
            else:
                file.write("\n" + redirect + " " + website )

def unblock_host():
    with open(host_path,'r+') as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any (website in line for website in website_list):
                file.write(line)
        file.truncate()
           


