import shutil
import os
currentdir = os.curdir
import sys

import grf_farm

# add dir to path so we can do relative import of the Polar Fox python content for integrity checks
sys.path.insert(0,currentdir)

dist_container_path = grf_farm.dist_container_path

def main():
    print("Preparing files for distribution")
    if os.path.exists(dist_container_path):
        print("Cleaning: removing", dist_container_path)
        shutil.rmtree(dist_container_path)
    os.mkdir(dist_container_path)

    for dir_name in ['firs', 'iron-horse', 'road-hog', 'unsinkable-sam']:
        dist_dir_path =  os.path.join(dist_container_path, dir_name)
        shutil.copytree(os.path.join(currentdir, 'src', dir_name), dist_dir_path)

    """
    for filename in ['LICENSE.txt', 'README.txt']:
        shutil.copy(os.path.join(currentdir, filename), os.path.join(dist_package_path, filename))
    """
    print("[DONE]")

if __name__ == '__main__':
    main()
