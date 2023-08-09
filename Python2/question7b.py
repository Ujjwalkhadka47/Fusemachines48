'''
 Create a function add_to_json that takes a filename and a dictionary as input. The
function should read the JSON data from the file, add the new dictionary to it, and
write the updated data back to the same file.

'''
import json

def add_to_json(filename, new_dict):
    """add the new_dict to the given json filename 

    Args:
        filename (str): filename
        new_dict (dict): dict to write the JSON into 
    """
    try:
        # Read existing JSON data from the file
        with open(filename, 'r') as file:
            # load the existing file 
            existing_data = json.load(file)
        
        # Append the new dictionary to the existing data
        existing_data.append(new_dict)
        
        # Write the updated data back to the same file
        with open(filename, 'w') as file:
            json.dump(existing_data, file, indent=4)
        
        print("Data added and updated successfully.")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON data from '{filename}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
new_data = {"name": "Luffy", "age": 19, "city": "East Blue"}
add_to_json("data.json", new_data)