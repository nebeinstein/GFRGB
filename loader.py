import os
import preproc as pp
def get_files_in(directory):
    """returns a list of files in the given directory"""
    return os.listdir(directory)

def process_image(filepath):
    """Processes a given image"""
    img = pp.load_image_as_grayscale(filepath)
    img = pp.autocrop_edges(img)
    img = pp.apply_blur(img)
    img = pp.circle_darkest(img)
    return img

def process_list(lis):
    """This takes a list of filepaths and processes each one"""
    return [process_image(x) for x in lis]
    

def process_all(directory):
    """Processess all of the images in a given directory"""
    return process_list(get_files_in(directory))
