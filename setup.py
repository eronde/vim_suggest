try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name = "py_word_suggest",
            description="py_word_suggest",
            long_description = """
Py-word-suggest is a library for fetching suggested words from a redis server in Python 3. 
""",
            license="""MIT""",
            version = "0.0.1",
            author = "",
            author_email = "",
            maintainer = "",
            maintainer_email = "",
            url = "",
            packages = ['py_word_suggest'],
            classifiers = [
              'Programming Language :: Python :: 3',
              ]
            )

