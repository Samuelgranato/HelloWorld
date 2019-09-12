from setuptools import setup

setup(name="my_hello_samuelgranato2",
      version="0.2",
      packages=['my_hello'],
      install_requires=[
          'numpy'
      ],
      scripts=['scripts/hello.py']
      )
