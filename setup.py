import setuptools
from govuk_elements_jinja_macros.version import Version


setuptools.setup(name='govuk-elements-jinja-macros',
                 version=Version('1.0.7').number,
                 description='GOV.UK elements Jinja macros',
                 packages=['govuk_elements_jinja_macros'],
                 package_data={'govuk_elements_jinja_macros': ['templates/*.html']}
                 )
