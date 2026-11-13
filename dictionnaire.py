#training on dictionnary
capital = {
    "France" : "Paris",
    "Germany": "Berlin",
}

travel_log = {
    "France":["Paris","Lille","Dijon"],
    "Germany":["Stuttgart","Berlin"]
}

print(travel_log["France"][1])

nested_list = ["A","B",["C","D"]]
print(nested_list[2])

travel_log = {
    "France":{
        'cities_visited':["Paris","Lille","Dijon"],
        'total_visits':5
    },
    "Germany":{
        'cities_visited':["Stuttgart","Berlin"],
        'total_visits':8
    }
    
}
print(travel_log["Germany"]["cities_visited"][1])

#The Secret Auction Program Instructions

bid_price = "yes"
members_bid = {}
while bid_price == "yes":
    name =input("What's your name? ")
    bid = int(input("What's your bid $ ? "))
    members_bid[name] = bid
    bid_price = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()

for name,bid in members_bid.items():
    if bid == max(members_bid.values()):
        print(f"The winner is {name} with a bid of ${bid}.")


