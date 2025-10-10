
email = input("enter your email:")

# loki@gmail.com
# index = 

username = email[:email.index("@")]
domain = email[email.index("@") + 1:]

print(f"your username is {username}" + f" and domainname is {domain} ")
print(f"yes ur in")