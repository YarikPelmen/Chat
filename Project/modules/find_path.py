import os


def find_path(name_file):
    abs_path = __file__.split("/")
    del abs_path[-1]
    abs_path = '/'.join(abs_path)
    abs_path = os.path.join(name_file)
    return abs_path
