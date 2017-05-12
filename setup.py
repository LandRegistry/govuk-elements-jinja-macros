import setuptools
from govuk_jinja_macros.version import Version


setuptools.setup(name='govuk-jinja-macros',
                 version=Version('1.0.0').number,
                 description='GOV.UK Jinja macros',
                 packages=['govuk_jinja_macros'],
                 install_requires=[],
                 zip_safe=False
                 )
