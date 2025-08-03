host_path = r"C:\Windows\System32\drivers\etc\hosts"  # Use "/etc/hosts" for Linux/Mac
redirect = "127.0.0.1"
sites = ["www.youtube.com", "youtube.com", "www.instagram.com", "instagram.com"]

def block():
    with open(host_path, "r+") as file:
        content = file.read()
        for site in sites:
            if site not in content:
                file.write(f"{redirect} {site}\n")
    print("Websites blocked!")

def unblock():
    with open(host_path, "r+") as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(site in line for site in sites):
                file.write(line)
        file.truncate()
    print("Websites unblocked!")

choice = input("1. Block\n2. Unblock\nChoose option: ")

if choice == "Block":
    block()
elif choice == "Unblock":
    unblock()
else:
    print("Invalid choice.")
