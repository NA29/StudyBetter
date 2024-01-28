import os
from google_images_search import GoogleImagesSearch

def getImage():

    # you can provide API key and CX using arguments,
    # or you can set environment variables: GCS_DEVELOPER_KEY, GCS_CX
    os.environ['GCS_DEVELOPER_KEY'] = 'Your_Developer_Key_Here'
    os.environ['GCS_CX'] = 'Your_Custom_Search_Engine_ID_Here'

    gis = GoogleImagesSearch()

    # define search params
    # option for commonly used search param are shown below for easy reference.
    # For param marked with '##':
    #   - Multiselect is currently not feasible. Choose ONE option only
    #   - This param can also be omitted from _search_params if you do not wish to define any value
    _search_params = {
        'q': 'car',
        'num': 10,
        'fileType': 'jpg|gif|png',
        'imgType': 'photo', ##
        'imgColorType': 'color' ##
    }

    # this will only search for images:
    gis.search(search_params=_search_params)

    # this will search and download:
    gis.search(search_params=_search_params, path_to_dir='./images')

    # this will search, download and resize:
    gis.search(search_params=_search_params, path_to_dir='./images', width=500, height=500)

    # search first, then download and resize afterwards:
    gis.search(search_params=_search_params)
    for image in gis.results():
        image.url  # image direct url
        image.referrer_url  # image referrer url (source) 
        
        image.download('./images')  # download image
        image.resize(500, 500)  # resize downloaded image

        image.path  # downloaded local file path
