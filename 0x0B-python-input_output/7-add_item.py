#!/usr/bin/python3
import sys
import json

# Assuming '5-save_to_json_file.py' and '6-load_from_json_file.py' exist in the same directory
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv
filename = "add_item.json"

# Open the file in 'r+' mode instead of 'a+'
with open(filename, 'r+', encoding="utf-8") as f:
    # Load existing data if any
    try:
        my_list = load_from_json_file(filename)
    except FileNotFoundError:
        my_list = []
    
    # Append command line arguments individually to the list
    my_list.extend(args[1:])
    
    # Save the updated list to the file
    save_to_json_file(my_list, filename)
