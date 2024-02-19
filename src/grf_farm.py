import os
currentdir = os.curdir

dist_container_path = os.path.join(currentdir, 'dist')

registered_grfs = ['firs', 'iron-horse', 'iron-ibex', 'road-hog', 'unsinkable-sam']

# chameleon templating goes faster if a cache dir is used; this specifies which dir is cache dir
chameleon_cache_dir = '.chameleon_cache'
