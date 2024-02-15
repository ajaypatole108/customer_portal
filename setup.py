from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in customer_portal/__init__.py
from customer_portal import __version__ as version

setup(
	name="customer_portal",
	version=version,
	description="In this app we making customisation related to customer portal",
	author="Ajay Patole",
	author_email="ajaypatole@dhuparbrothers.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
