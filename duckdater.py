import requests
import argparse
from termcolor import colored
import argparse

token = "<REPLACE WITH YOUR TOKEN>"

menu_options = {
    1: 'Update DNS entry',
    2: 'Clear DNS entry',
    3: 'Exit',
}

text = 'Update DNS info on DuckDNS via terminal. The domain can be a single domain - or a comma separated list of domains. The domain does not need to include the .duckdns.org part of your domain, just the subname.'

# Initiate the parser with description text

parser = argparse.ArgumentParser(description=text)

args = parser.parse_args()


print("______ _   _ _____  _   __    _       _            ")
print("|  _  \ | | /  __ \| | / /   | |v1.0 | |by stefexec")
print("| | | | | | | /  \/| |/ /  __| | __ _| |_ ___ _ __ ")
print("| | | | | | | |    |    \ / _` |/ _` | __/ _ \ '__|")
print("| |/ /| |_| | \__/\| |\  \ (_| | (_| | ||  __/ |   ")
print("|___/  \___/ \____/\_| \_/\__,_|\__,_|\__\___|_|   ")
print()

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def updatedns():
     print()
     print(colored("DuckDNS updater started!", "green"))
     print()
     
     domains = input("Choose Domain(s) to update: ")
     ip4 = input("Enter new IPv4: ")
     print()
     print(colored("Response from DuckDNS: ", "cyan"))
     r = requests.get('https://www.duckdns.org/update?domains=' + domains + '&token=' + token + '&ip=' + ip4 + '&verbose=true')
     print(r.text)
     print()
     exit()

def cleardns():
     print()
     print(colored("DNS settings will be reset!", "red"))
     print()
     domainsclear = input("Choose Domain(s) to clear: ")
     print()
     r =requests.get('https://www.duckdns.org/update?domains=' + domainsclear + '&token=' + token + '&verbose=true&clear=true')
     print(colored("Response from DuckDNS: ", "cyan"))     
     print(colored(r.text))
     print()
     exit()

if __name__=='__main__':

    while(True):
        print_menu()
        option = ''
        try:
            print()
            option = int(input('Choose an Option: '))
        except:
            print()
            print(colored('Input not recognized!', 'red'))
            print()
            
        #gewählte Option überprüfen
        
        if option == 1:
           updatedns()
        elif option == 2:
            cleardns()
        elif option == 3:
            print()
            print('Glückauf!')
            print()
            exit()
        else:
            print('Choose a number between 1 and 3. Believe in yourself! You can do it!')
            print()








