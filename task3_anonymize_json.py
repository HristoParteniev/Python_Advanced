"""imports"""
import json
import os

if __name__ == '__main__':

    # Define the source and target file paths
    src_path = os.path.join(os.path.expanduser("~"),
    'OneDrive - Adastra, s.r.o\\Desktop\\users_1k.JSON')
    tgt_path = os.path.join(os.path.expanduser("~"),
    'OneDrive - Adastra, s.r.o\\Desktop\\users_1k_edited_Hristo_Parteniev.JSON')

    def update_name_keys(data):
        """Recursively updates 'name' keys in JSON-like data to 'null'."""
        if isinstance(data, dict):
            # Check if 'name' is a key in the dictionary
            if 'name' in data:
                data['name'] = 'null'

            # Recursively process all dictionary values
            for value in data.values():
                update_name_keys(value)

        elif isinstance(data, list):
            # Recursively process all items in the list
            for item in data:
                update_name_keys(item)

    def process_json_file(src_path):
        """Reads JSON file, updates 'name' keys, and returns modified data."""
        with open(src_path, 'r', encoding='utf-8') as file:
            data = json.load(file)  # Load the JSON data
            update_name_keys(data)  # Update the 'name' keys
        return data

    # Process the JSON file and update the 'name' fields
    try:
        # Read source JSON file
        updated_data = process_json_file(src_path)

        # Write updated data to target file
        with open(tgt_path, 'w', encoding='utf-8') as file:
            json.dump(updated_data, file, indent=2)

        # Printing data on terminal for verification
        print(json.dumps(updated_data, indent=2))

    except FileNotFoundError as e:
        # Handle the case where the file does not exist
        print(f"Error: The file '{src_path}' does not exist.")
        raise  e

    except json.JSONDecodeError as e:
        # Handle the case where the file is not a valid JSON
        print(f"Error: The file '{src_path}' is not a valid JSON or is corrupted.")
        raise e

    except IOError as e:
        # Handle other I/O related errors, such as permission issues
        print(f"Error: An I/O error occurred while trying to read '{src_path}'.")
        raise e

    except Exception as e:
        # Catch any other unexpected exceptions
        print(f"An unexpected error occurred: {e}")
        raise e
