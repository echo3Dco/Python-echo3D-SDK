from echo3d_api import *
import argparse
from render import *

"""
Parse user arguments 
"""
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('api_key', type=str,
                        help='Your Echo3D api key')
    parser.add_argument('security_key', type=str,
                        help='Your Echo3D security key')
    
    args = parser.parse_args()
    if error_handle(args) == -1:
        return -1
    
    # Retrieve 3d models via Echo3D API
    api = Echo3DAPI(api_key=args.api_key, security_key=args.security_key)
    model_list = api.retrieve_model_info()

    # Download and render a 3d model specified by user using Python Vedo Library
    renderer = Renderer('downloads', api.entries)
    entry = user_prompt(model_list)
    file_format = api.retrieve(entry)

    if file_format == 'obj':
        renderer.obj_render(entry)
    elif file_format == 'glb':
        renderer.glb_render(entry)
    else:
        print("File format " + file_format + " not supported yet")

    return 0

"""
User prompt to choose which 3d model to open with
"""
def user_prompt(model_list: dict):
    print()
    print("<=== List of available 3d models ===>")
    for key in model_list:
        print(key + ": " + model_list[key][1])
    print("<===================================>")
    print()
    
    user_choice = input("Please select a 3d model to display by specifying the number from the list above => ")
    while user_choice not in model_list:
        print("[ERROR] Number invalid. Please specify the number that is available!")
        user_choice = input("Please select a 3d model to display by specifying the number from the list above => ")

    print("Model selected successfully. Preparing for rendering")
    return model_list[user_choice][0]

"""
TO BE EXPANDED. Handle argument errors
"""
def error_handle(args):
    return 0

if __name__ == '__main__':
    main()

