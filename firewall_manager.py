import os

def activate_ufw():
    res = os.popen("sudo ufw enable").read()
    result = print(res)
    return result

def menu():
	print("1.Get firewall status")
	print("2.Set firewall rules")
	print("3.Delete rules")
	print("4.Reload rules")
	print("5.Exit")

def rules_menu():
	print("\t\t1.Enable perticular port")
	print("\t\t2.Disable perticular port")
	print("\t\t3.Block host/IP")
	print("\t\t4.Allow host/IP")
	print("\t\t5.Check rules")
	print("\t\t6.Exit")
	
def rules():
	while True:
		activate_ufw()
		rules_menu()
		choice = input("Enter your choice :  ")
		if choice == '1':
			port = input("Enter the port to be enabled :  ")
			command = f'sudo ufw allow {port}'
			result = os.popen(command).read()
			print(result)
		elif choice == '2':
			port = input("Enter the port to be disabled :  ")
			command = f'sudo ufw deny {port}'
			result = os.popen(command).read()
			print(result)
		elif choice == '3':
			ip = input("Enter the IP to block :  ")
			command = f'sudo ufw deny from {ip}'
			result = os.popen(command).read()
			print(result)
		elif choice == '4':
			ip = input("Enter the IP to block :  ")
			command = f'sudo ufw allow from {ip}'
			result = os.popen(command).read()
			print(result)
		elif choice == '5':
			command = 'sudo ufw status numbered'
			result = os.popen(command).read()
			print(result)
		elif choice == '6':
			break
		else:
			print("Invalid input")	
def delete_rules():
	command = 'sudo ufw status numbered'
	result = os.popen(command).read()
	print(result)
	indx = input("Enter the index number of the rule to be deleted :  ")
	command = f'sudo ufw delete {indx}'
	result = os.popen(command).read()
	print(result)
while True:
	activate_ufw()
	menu()
	ch = input("Enter your choice :  ")
	if ch == '1':
		command = 'sudo ufw status'
		result = os.popen(command).read()
		print(result)
	elif ch == '2':
		rules()
	elif ch == '3':
		delete_rules()
	elif ch == '4':
		command = 'sudo ufw reload'
		result = os.popen(command).read()
		print(result)
	elif ch == '5':
		break
	else:
		print("Invalid input")
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
