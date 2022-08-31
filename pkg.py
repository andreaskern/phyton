# apk, apt, dnf, pip, ... but just call it pkg

import pkg_resources
_pkgs = pkg_resouces.wokring_set
pkgs = list(map(str,_pkgs))

# todo 
'''
pkg.add('name') # ensures it is installed
pkg.doc('name')
pkg.deps('name')
'''

# idea
'''
replace `import x`
with `ensure x` that imports and installs packages
'''

