import requests
import argparse
from termcolor import colored
import argparse
import json

with open("config_file.json") as json_data_file:
    config = json.load(json_data_file)
    

token_parsed = config["token"]


menu_options = {
    1: 'Update DNS entry',
    2: 'Clear DNS entry',
    3: 'Set new token',
    4: 'Exit',
}

text = 'Update DNS info on DuckDNS via terminal. The domain can be a single domain - or a comma separated list of domains. The domain does not need to include the .duckdns.org part of your domain, just the subname.'

# Initiate the parser with description text

parser = argparse.ArgumentParser(description=text)

args = parser.parse_args()


print("______ _   _ _____  _   __    _       _            ")
print("|  _  \ | | /  __ \| | / /   | |v1.1 | |by stefexec")
print("| | | | | | | /  \/| |/ /  __| | __ _| |_ ___ _ __ ")
print("| | | | | | | |    |    \ / _` |/ _` | __/ _ \ '__|")
print("| |/ /| |_| | \__/\| |\  \ (_| | (_| | ||  __/ |   ")
print("|___/  \___/ \____/\_| \_/\__,_|\__,_|\__\___|_|   ")
print()

def set_token():
    global token_parsed
    global config
    print()
    print("Current token is: " + token_parsed + "\n")
    
    token_new = input("Please set a new token: ")
    config["token"] = token_new
    
    #write new token to config file
    with open("config_file.json", "w") as write_file:
    	json.dump(config, write_file)
    #read fresh token 	
    with open("config_file.json") as json_data_file:
     config = json.load(json_data_file)
    	
    token_parsed = config["token"]	
    
    print()	
    print(colored("Set new token as: " + token_new + "\n", "green"))
    main()	

def print_menu():
    print("=====================Main Menu=====================" + "\n")
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
     r = requests.get('https://www.duckdns.org/update?domains=' + domains + '&token=' + token_parsed + '&ip=' + ip4 + '&verbose=true')
     print(r.text)
     print()
     exit()

def cleardns():
     print()
     print(colored("DNS settings will be reset!", "red"))
     print()
     domainsclear = input("Choose Domain(s) to clear: ")
     print()
     r =requests.get('https://www.duckdns.org/update?domains=' + domainsclear + '&token=' + token_parsed + '&verbose=true&clear=true')
     print(colored("Response from DuckDNS: ", "cyan"))     
     print(colored(r.text))
     print()
     main()

     
     
def main():
      
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

            
        #check chosen option
        
        if option == 1:
           updatedns()
        elif option == 2:
           cleardns()
        elif option == 3:
           set_token()
        elif option == 4:
            print()
            print('Glückauf!')
            print()
            exit()
        else:
            print('Choose a number between 1 and 3. Believe in yourself! You can do it!')
            print()
       

if __name__=='__main__':

    
 if token_parsed != "0":
  main()
 else:
  set_token()
 

            




