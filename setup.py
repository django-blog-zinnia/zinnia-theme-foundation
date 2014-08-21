import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name = 'zinnia-theme-foundation',
    version = '1.0.1',
    packages = ['zinnia_foundation'],
    include_package_data = True,
    license = 'GPL',
    description = 'A theme with Zurb Foundation for django-blog-zinnia.',
    long_description = README,
    url = 'https://github.com/gustavi/zinnia-theme-foundation',
    author = 'gustavi',
    author_email = 'augustin.laville@gustavi.net',
    platforms = 'any',
    install_requires = [
        'django-blog-zinnia',
    ],
    classifiers = [
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
    zip_safe = False
)

