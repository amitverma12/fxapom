from setuptools import setup, find_packages

setup(name='fxapom',
      version='1.8.0',
      description='Mozilla Firefox Accounts Page Object Model',
      long_description=open('README.rst').read(),
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
          'Operating System :: POSIX',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: MacOS :: MacOS X',
          'Topic :: Software Development :: Testing',
          'Topic :: Utilities',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7'],
      keywords='mozilla',
      author='Mozilla Web QA',
      author_email='mozwebqa@mozilla.org',
      url='https://github.com/mozilla/fxapom',
      license='MPL 2.0',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      install_requires=['PyFxA==0.2.0'],
      include_package_data=True)
