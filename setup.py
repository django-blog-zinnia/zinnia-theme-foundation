"""Setup script of zinnia-theme-foundation"""
from setuptools import find_packages
from setuptools import setup

import zinnia_foundation


setup(
    name='zinnia-theme-foundation',
    version=zinnia_foundation.__version__,
    license=zinnia_foundation.__license__,

    description='A theme with Zurb Foundation for django-blog-zinnia.',
    long_description=open('README.md').read(),
    keywords='django, blog, weblog, zinnia, theme, skin, foundation',

    url=zinnia_foundation.__url__,
    author=zinnia_foundation.__author__,
    author_email=zinnia_foundation.__email__,

    packages=find_packages(exclude=['demo_zinnia_foundation']),
    classifiers=[
        'Framework :: Django',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    zip_safe=False,
    include_package_data=True
)
