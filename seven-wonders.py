import requests
from single_wonder import get_single_wonder

WONDERS = ["Great Wall of China","Petra","Colosseum","Chichen Itza","Machu Picchu","Taj Mahal","Christ the Redeemer"]
all_wonders = {}

for wonder in WONDERS:
    all_wonders[wonder] = get_single_wonder(wonder)
print(all_wonders)


#print("The value of response.json()", response_body)
#------------------\\\\\\\\------------------------###

#print(f"The lat and lon of {wonder} is {response_body["lat"]}, {response_body["lon"]}")
###----------------###
#print(f"The display name of {search_term} is {response_body[0]["display_name"]}")
#print(f"{search_term} is a {response_body[0]["type"]} {response_body[0]["class"]}")

