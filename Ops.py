import os

# Declare and initialize variables
name = "Deqa Hussein"
age = 23
city = "Twin cities"

# Print variable values using the print() function
print("Name:", name)
print("Age:", age)
print("City:", city)

# Execute bash commands using os.system() and print the output
# Bash command: whoami
whoami_result = os.popen("whoami").read().strip()
print("Current user:", whoami_result)

# Bash command: ip a
ip_a_result = os.popen("ip a").read().strip()
print("IP address information:\n", ip_a_result)

# Bash command: lshw -short
lshw_result = os.popen("lshw -short").read().strip()
print("Hardware information:\n", lshw_result)
