import codecs
import shutil
import os
currentdir = os.curdir
import sys
import subprocess
from packaging.version import Version, parse

import grf_farm

# add dir to path so we can do relative import of the Polar Fox python content for integrity checks
sys.path.insert(0,currentdir)

dist_container_path = grf_farm.dist_container_path

chameleon_cache_path = os.path.join(currentdir, grf_farm.chameleon_cache_dir)
if not os.path.exists(chameleon_cache_path):
    os.mkdir(chameleon_cache_path)
os.environ['CHAMELEON_CACHE'] = chameleon_cache_path

from chameleon import PageTemplateLoader
docs_templates = PageTemplateLoader(os.path.join(currentdir, 'src', 'templates'), format='text')

def render_grf_index_pages(grf_name, dist_dir_path):
    print("Adding index page for", grf_name)
    template = docs_templates['grf_index_page.pt']

    distributed_docs_versions = [dir_name for dir_name in os.listdir(dist_dir_path) if os.path.isdir(os.path.join(dist_dir_path, dir_name))]
    # note use of parse from python packaging library, this provides sorting on version numbers which don't sort desirably as strings, and can't be treated as int due to e.g. '-alpha-' versions
    distributed_docs_versions = sorted(distributed_docs_versions, key=lambda x: parse(x))

    grf_index_page_html = template(grf_farm=grf_farm, grf_name=grf_name, distributed_docs_versions=distributed_docs_versions)
    grf_index_page_file = codecs.open(os.path.join(dist_dir_path, 'index.html'), 'w', 'utf8')
    grf_index_page_file.write(grf_index_page_html)
    grf_index_page_file.close()

def main():
    print("Preparing files for distribution")
    if not os.path.exists(dist_container_path):
        print("Creating", dist_container_path)
        os.mkdir(dist_container_path)

    for grf_name in grf_farm.registered_grfs:
        dist_dir_path =  os.path.join(dist_container_path, grf_name)
        src_dir_path = os.path.join(currentdir, 'src', grf_name)
        print("Syncing dirs for", grf_name)
        # rsync is used as it's substantially faster than python copytree, both in the case of copying everything, and even faster if only a partial copy is needed
        subprocess.call(['rsync', '-a', '--delete', src_dir_path, dist_container_path])
        render_grf_index_pages(grf_name, dist_dir_path)

    """
    # copied from Polar Fox, not needed here?
    for filename in ['LICENSE.txt', 'README.txt']:
        shutil.copy(os.path.join(currentdir, filename), os.path.join(dist_package_path, filename))
    """
    print("[DONE]")

if __name__ == '__main__':
    main()
