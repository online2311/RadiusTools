#!/usr/bin/python


from setuptools import setup, find_packages
import radiustools

version = radiustools.__version__

install_requires = [
    'six>=1.8.0',
    'Twisted>=13.0.0'
]
install_requires_empty = []

package_data={}


setup(name='radiustools',
      version=version,
      author='ZhangJing',
      author_email='ZhangJing@outlook.com',
      url='https://github.com/online2311/RadiusTools',
      license='GPL',
      description='RADIUS tools',
      long_description=open('README.md').read(),
      classifiers=[
       'Development Status :: 6 - Mature',
       'Intended Audience :: Developers',
       'Programming Language :: Python :: 2.6',
       'Programming Language :: Python :: 2.7',
       'Topic :: Software Development :: Libraries :: Python Modules',
       'Topic :: System :: Systems Administration :: Authentication/Directory',
       ],
      packages=find_packages(),
      package_data=package_data,
      keywords=['radius', 'AAA','authentication','accounting','authorization','toughradius'],
      zip_safe=True,
      include_package_data=True,
      install_requires=install_requires,
)