import json
# message to display when this script is called from node script
# print("This message is from python file: Hello Node!! Thanks for calling. :) \n")

# json packet
with open('letter_number.json') as json_data:
    for entry in json_data:
        print(entry)
