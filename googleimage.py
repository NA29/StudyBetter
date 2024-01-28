import os
from google_images_search import GoogleImagesSearch

def getImage(query):
    
    download_path = './images'

    gis = GoogleImagesSearch('AIzaSyBUPMaep14tCPHEc29Uw9BdkBdpmbclp6Y', '45795065575ed4290')
    # define search params
    # option for commonly used search param are shown below for easy reference.
    # For param marked with '##':
    #   - Multiselect is currently not feasible. Choose ONE option only
    #   - This param can also be omitted from _search_params if you do not wish to define any value
    _search_params = {
        'q': query,
        'num': 1,
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
        image_name = image.url.split('/')[-1]  # Extracting image name from URL
        # old_image_path = os.path.join(download_path, image_name)
        # new_image_path = os.path.join(download_path, f"{query}.jpg")  # New name for the image
        # os.rename(old_image_path, new_image_path)  # Rename the image


        image.path  # downloaded local file path
        return image


if __name__ == '__main__':
    getImage("friend")