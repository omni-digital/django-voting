from distutils.core import setup

setup(
    name='django-voting',
    version='0.2.1',
    description='Generic voting application for Django',
    author='Jonathan Buchanan',
    author_email='jonathan.buchanan@gmail.com',
    maintainer='Jannis Leidel',
    maintainer_email='jannis@leidel.info',
    url='https://github.com/pjdelport/django-voting',
    packages=[
        'voting',
        'voting.migrations',
        'voting.templatetags',
        'voting.tests',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
)
