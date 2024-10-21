import json
import os

def load_json_file():

    folder_name=input('Enter the folder name where your JSON file is located: ')
    file_name='jayasri_sanka_adoptions.json'    
    file_path_way='C:/Users/jayas/OneDrive/Desktop/files_assignment/files_assignment/jayasri_sanka_adoptions.json'
    try:
        with open(file_path_way, 'r') as file:
            data = json.load(file)
            print('file loaded succesfully')
        return data    
    except FileNotFoundError as fnf_error:
        print(f'file{file_path_way} not found')
    except json.JSONDecodeError as json_error:
        print(f"Error decoding JSON: {json_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
data = load_json_file()
#print(data[10])