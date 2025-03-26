# -- Print Versions -------------------------------------------------------

import sys
print ('python version: ' + str(sys.version))

from sphinx import __version__ as sphinx_version
print ('sphinx version: ' + str(sphinx_version))

from sphinx_ifelse import __version__ as sphinx_ifelse_version
print ('sphinx_ifelse version: ' + str(sphinx_ifelse_version))

# -- General configuration ------------------------------------------------

project = 'Test Project'

extensions = [
   'sphinx_ifelse',
]

# -- extension configuration: ifelse --------------------------------------

ifelse_variants = {
   'html': True,
   'latex': False,
   'pdf': False,
   'epub': False,
   'l1': 3,
   'l2': 3,
   'l3': 3,
}
