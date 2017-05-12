import setuptools
from govuk_elements_jinja_macros.version import Version


setuptools.setup(name='govuk-elements-jinja-macros',
                 version=Version('1.0.0').number,
                 description='GOV.UK elements Jinja macros',
                 packages=['govuk_elements_jinja_macros'],
                 install_requires=[],
                 zip_safe=False
                 )
