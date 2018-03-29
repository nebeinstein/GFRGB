import os
import preproc as pp
def get_files_in(directory):
    """returns a list of files in the given directory"""
    return [directory+ "/" + x for x in os.listdir(directory)]

def clean_file_list(lis):
    return [x for x in lis if x.endswith('.tif')]

def set_preproc_edge_cut(val):
    pp.edge_cut=val

def set_preproc_bottom_cut(val):
    pp.bottom_cut = val
    
def set_preproc_top_cut(val):
    pp.top_cut = val
    
def set_preproc_left_cut(val):
    pp.left_cut = val
    
def set_preproc_right_cut(val):
    pp.right_cut = val
    

def process_image(filepath):
    """Processes a given image"""
    img = pp.load_image_as_grayscale(filepath)
    img = pp.autocrop_edges(img)
    img = pp.apply_blur(img)
    img = pp.circle_darkest(img)
    pp.save_image(filepath, img)
    return img

def process_list(lis):
    """This takes a list of filepaths and processes each one"""
    return [process_image(x) for x in lis]
    
def process_all(directory):
    """Processess all of the images in a given directory"""
    return process_list(get_files_in(directory))
