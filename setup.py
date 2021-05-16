from setuptools import setup

setup(
 name = 'enginemonitor',
 version = '1.0.0',
 license = 'license name, e.g. MIT',
 description = '',
 author = 'Benny Carbajal',
 author_email = 'benny.carbajalb@gmail.com',
 package_dir={'':'src'},
 install_requires=[
  'psutil',
  'pymongo',
  'wmi'
 ],
 classifiers=[
  'Development Status :: 3 - Alpha',
  'Programming Language :: Python :: 3.7',
  'Natural Language :: English',
  'Intended Audience :: Developers',
  'License :: OSI Approved :: MIT License',
  'Operating System :: Operating System :: OS Independent',
  'Programming Language :: Python',
  'Programming Language :: Python :: 3',
  'Topic :: Utilities',
 ]
)