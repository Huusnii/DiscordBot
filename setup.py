from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='DiscordGalleryBot',
    version='0.0.1',
    description='Bot to gather all the attachment (and URL) and send it to one channel',
    long_description=readme,
    author='Huusnii',
    author_email='',
    url='https://github.com/Huusnii/DiscordGalleryBot',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)