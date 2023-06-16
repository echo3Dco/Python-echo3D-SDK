import requests
import urllib
import json
import os
from copy import deepcopy

class Echo3DAPI:

    def __init__(self, api_key: str, security_key: str):
        self.main_url = 'https://api.echo3D.com/query?'
        self.api_key = api_key
        self.security_key = security_key
        self.check_path_exist('downloads')
        self.base_params = {'key': self.api_key, 'secKey': self.security_key}
        self.entries = self.get_json_entries(self.base_params)

    def check_path_exist(self, pathname):
        if not os.path.exists(pathname):
            os.makedirs(pathname)

    def create_url(self, params):
        return self.main_url + urllib.parse.urlencode(params)

    """
    Get json responses from Echo3D API
    """
    def get_json_entries(self, params):
        url = self.create_url(params)
        json_response = urllib.request.urlopen(url)
        data = json.loads(json_response.read())
        return data
    
    """
    Download a file via Echo3D url 
    """
    def download_file(self, params):
        url = self.create_url(params)
        r = requests.get(url, allow_redirects=True)
        return r
    
    def retrieve(self, entry):
        hologram = self.entries["db"][entry]["hologram"]
        self.check_path_exist('downloads/' + entry)
        file_format = hologram['filename'][-3:]

        if file_format == 'obj':
            self.retrieve_obj(entry)
        elif file_format == 'glb':
            self.retrieve_glb(entry)

        return file_format

    """
    Download a 3D model with .obj file format based on entry id
    """
    def retrieve_obj(self, entry):
        hologram = self.entries["db"][entry]["hologram"]

        # Download the main 3d file
        params = deepcopy(self.base_params)
        params['file'] = hologram['storageID']
        result = self.download_file(params)
        open('downloads/' + entry + '/' + hologram['filename'], 'wb').write(result.content)

        # Download all texture files
        for i in range(len(hologram['textureStorageIDs'])):
            params = deepcopy(self.base_params)
            params['file'] = hologram['textureStorageIDs'][i]
            result = self.download_file(params)
            open('downloads/' + entry + '/' + hologram['textureFilenames'][i], 'wb').write(result.content)

        # Download material file
        params = deepcopy(self.base_params)
        params['file'] = hologram['materialStorageID']
        result = self.download_file(params)
        open('downloads/' + entry + '/' + hologram['materialFilename'], 'wb').write(result.content)

    """
    Download a 3D model with .glb file format based on entry id
    """
    def retrieve_glb(self, entry):
        hologram = self.entries["db"][entry]["hologram"]

        # Download the main 3d file
        params = deepcopy(self.base_params)
        params['file'] = hologram['storageID']
        result = self.download_file(params)
        open('downloads/' + entry + '/' + hologram['filename'], 'wb').write(result.content)

    """
    Retrieve all model info. Return a mapping list of all 3d models based on api and security key
    """
    def retrieve_model_info(self):
        model_list = {}
        i = 1
        for entry in self.entries["db"]:
            model_list[str(i)] = (entry, self.entries["db"][entry]["hologram"]["filename"])
            i += 1

        return model_list