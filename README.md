# GOV.UK Elements Jinja macros

## Assumptions
You are using Python/Flask and WTForms via Flask-WTF. These templates may work with Jinja and WTForms standalone but this has not been tested.

## Caveats
The macros only cater for relatively simple usages of the form markup. If you need to do something that isn't catered for - just break out and write the HTML. These templates are here to help you, but stop using them as soon as they stop helping you, don't battle with them... Instead, refer directly to http://govuk-elements.herokuapp.com/form-elements/

## Using the templates from within your Flask app
In order to use these templates, you need to configure your Flask app to load templates from sources other than your app. This is done with the following snippet:

```
app.jinja_loader = PrefixLoader({
    'app': PackageLoader('your_main_frontend_app_here'),
    'govuk_elements_jinja_macros': PackageLoader('govuk_elements_jinja_macros'),
})
```

This will mean that templates from your main app will now be available on the `app` prefix. For example, `{% extends "layout.html" %}` would have to become `{% extends "app/layout.html" %}`. Templates from this repository would be used like `{% from 'govuk_elements_jinja_macros/form.html' import element %}`

## Working on the templates
If you want to work on templates in the package from within the Land Registry common devenv you will need to follow the steps below.

> _Background: What you are aiming to do is to override the package which is installed from Git with a local copy of it while you are doing development work. However, due to a quirk of Docker's filesystems, `pip` is unable to install the local copy of the module over the top of the one that is already there. To work around this we have to mount a new volume over the top of the location where the module is installed. Like this:_

**Step 1**)
Add the following to your `dev-env-project/configuration.yml` file:
```
govuk-elements-jinja-macros:
  repo: git@github.com:LandRegistry/govuk-elements-jinja-macros.git
  branch: master
```

**Step 2**)
In the `docker-compose-fragment.yml` of your Flask frontend app, add the following to the `volumes` list:
```
- /vagrant/apps/govuk-elements-jinja-macros/govuk_elements_jinja_macros:/lib/python3.4/site-packages/govuk_elements_jinja_macros
```

This will mount the checked out copy of the repository over the top of where `pip` had installed the module to previously. Thereby allowing you to edit it whilst using it installed in your Flask app.

> Credit goes to [@sdchapman](https://github.com/sdchapman) for this ingenious idea. Thanks!
