dishndic = {
    "idli": "kerala",
    "dosa": "tamilnadu",
    "biryani": "hyderabad",
    "dal": "punjab",
    "samosa": "delhi"
}
print(dishndic)
print(dishndic["idli"])


del dishndic["dosa"] 
print(dishndic.get("dosa"))

print(dishndic.keys()) 
print(dishndic.items()) # returns key-value pairs like tuples
dishndic["papuri"] = "mumbai" # 
print(dishndic)

dishndics = {
    "idli": "kerala",
    "dosa": "tamilnadu",
    "biryani": "hyderabad",
    "dal": "punjab",
    "samosa": "delhi"
}
dishndic = {
    "idli": "kerala",
    "dosa": "tamilnadu",
    "biryani": "hyderabad",
    "dal": "punjab",
    "samosa": "delhi",
}

dishndics.update(dishndic) 