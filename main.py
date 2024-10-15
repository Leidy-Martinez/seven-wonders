from single_wonder import get_single_wonder

WONDERS = [
    "Great Wall of China", 
    "Petra", 
    "Colosseum",
    "Chichen Itza", 
    "Machu Picchu", 
    "Taj Mahal", 
    "Christ the Redeemer"
]


###############################
# Problem Set - single wonder #
###############################

print(get_single_wonder("Great Wall of China"))

####################################################
# Extra Challenge - handling list of wonders #
####################################################

all_wonders = {}

for wonder in WONDERS:
  result = get_single_wonder(wonder)
  all_wonders[wonder] = result

# Using dictionary comprehension instead of a loop:
# all_wonders = { wonder: get_single_wonder(wonder) for wonder in WONDERS }

print(all_wonders)
