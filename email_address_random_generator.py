"""
I wrote this program to generate a list of random fake e-mail addresses for practicing parsing webpages. 
I was working my way through chapter 8 of Bradford Tuckfield's excellent "Dive Into Data Science" book-- 
(No Starch Press, 2023), when I came across a couple of broken hyperlinks, the second of which was intended
to link to a page where there was a list of email addresses to practice using regular expression searches on,
so I ended up writing a little program that pulls names and domains from csv files and generates random e-mail
addresses. I generated the csv files with words and phrases from my own brain, stream-of-conscious-style.

The program uses the random library to generate random integers and then uses those random integers to call the index
locations of several lists of words in order to generate the list. The program prompts the user to enter the number
of addresses they would like to generate.

Note: If you modify or add to the files opened in this program, you can change what words the program uses to generate
the e-mail addresses.
"""

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
