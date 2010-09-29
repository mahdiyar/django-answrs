from setuptools import setup, find_packages

setup(
    name='django-answrs',
    description='A generic Djnago app to create a question and answer site',
    keywords='django, yahoo, answers',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    version="1.1",
    author="Agiliq Solutions",
    author_email="hello@agiliq.com",
    classifiers = ['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: GNU General Public License (GPL)',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Internet :: WWW/HTTP',
                   'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
                   'Topic :: Internet :: WWW/HTTP :: WSGI',
                   'Topic :: Software Development :: Libraries :: Application Frameworks',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   ],
    url="http://www.agiliq.com/",
    license="BSD",
    platforms=["all"],
)
