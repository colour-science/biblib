from setuptools import setup

setup(
    name='biblib-simple',
    version='0.1.2',
    description='Simple, correct BibTeX parser and algorithms',
    url='https://github.com/colour-science/biblib',
    author='Austin Clements',
    author_email='colour-science@googlegroups.com',
    packages=['biblib'],
    keywords=['bibtex', 'tex'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Database',
        'Topic :: Text Processing',
    ],
    long_description=open('README.md').read(),
)
