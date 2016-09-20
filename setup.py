import os
import sys
from distutils.core import Extension, setup
from Cython.Distutils import build_ext
import numpy as np

platform_supported = False
for prefix in ['darwin', 'linux', 'bsd']:
    if prefix in sys.platform:
        platform_supported = True
        include_dirs = [
            '/usr/include',
            '/usr/local/include',
        ]
        lib_dirs = [
            '/usr/lib',
            '/usr/local/lib',
        ]
        if 'CPATH' in os.environ:
            include_dirs += os.environ['CPATH'].split(':')
        if 'LD_LIBRARY_PATH' in os.environ:
            lib_dirs += os.environ['LD_LIBRARY_PATH'].split(':')
        break

if sys.platform == "win32":
    platform_supported = False

if not platform_supported:
    raise NotImplementedError(sys.platform)

setup(
    name="octomap",
    version="0.5",
    license = "BSD",
    packages=["octomap"],
    ext_modules=[Extension(
        "octomap",
        ["octomap/octomap.pyx"],
        include_dirs = [np.get_include()],
        library_dirs = lib_dirs,
        libraries=[
                "dynamicedt3d",
                "octomap",
                "octomath"
                ],
        language="c++")],
    cmdclass={'build_ext': build_ext},
    )
