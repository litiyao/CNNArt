from setuptools import setup
import sys

def readme():
    with open('README.md') as f:
        return f.read()

if sys.argv[-1] == 'test':
    setup(name='CNNArt',
          version='1.0',
          description='MR artifact detection',
          long_description=readme(),
          classifiers=[
            'Development Status :: Beta',
            'License :: Apache License 2.0',
            'Programming Language :: Python :: 2.7',
            'Topic :: CNN',
          ],
          keywords='CNN, artifacts, motion, multiclass',
          url='https://github.com/thomaskuestner/CNNArt',
          author='kSpace Astronauts',
          author_email='thomas.kuestner@iss.uni-stuttgart.de',
          license='Apache2',
          setup_requires=['pytest-runner'],
          tests_require=['pytest'],
          include_package_data=True,
          zip_safe=False)
    sys.exit()
