import random

names_obj = open('names.csv', 'r')
names = names_obj.readlines()
for i in range(50):
    names[i] = names[i].strip()

domains_obj = open('domains.csv', 'r')
domains = domains_obj.readlines()
for i in range(50):
    domains[i] = domains[i].strip()

endings_obj = open('endings.csv', 'r')
endings = endings_obj.readlines()
for i in range(6):
    endings[i] = endings[i].strip()

how_many = int(input("How many email addresses would you like to generate? "))
email_address_list = []
for i in range(how_many):
    rand_name = random.randint(0,49)
    rand_domain = random.randint(0,49)
    rand_ending = random.randint(0,5)
    email_name = names[rand_name]
    email_domain = domains[rand_domain]
    email_ending = endings[rand_ending]
    email_address = f"{email_name + "@" + email_domain + email_ending}"
    email_address_list.append(email_address)

print("Okay, here you go, a mighty fine list of e-mail addresses:\n")
for address in email_address_list:
    print(address)
print()
print("Thanks for your patronage! Come again!")