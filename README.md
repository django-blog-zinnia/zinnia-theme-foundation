Zinnia-theme-foundation
=======================

Zinnia-theme-foundation is a python package providing a theme builded on [Zurb Foundation 5](http://foundation.zurb.com) for [django-blog-zinnia](https://github.com/Fantomas42/django-blog-zinnia). Inspired by the [zinnia-theme-boostrap](https://github.com/Fantomas42/zinnia-theme-bootstrap).

Getting Start
-------------

### Download the package

The *Zinnia-theme-foundation* package required *django* and *django-blog-zinnia*.

You can install *zinnia-theme-foundation* with pip :

```
pip install zinnia-theme-foundation
```

If you want the dev version :

```
pip install git+git://github.com/gustavi/zinnia-theme-foundation.git
```

### Add the theme in django

Edit you `settings.py` and add *zinnia_foundation* in your `INSTALLED_APP` **BEFORE** the zinnia app to bypass the loading of the Zinnia's templates :

```python
INSTALLED_APPS = (
    ...
    'zinnia_foundation', # BEFORE the "zinnia" app
    ...
    'zinnia',
)
```

You need to use the `django.template.loaders.eggs.Loader` template loader if you have installed the package as an egg.

At the end of your `settings.py` :

```python
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)
```

or

```python
TEMPLATE_LOADERS += (
    'django.template.loaders.eggs.Loader',
)
```

Your theme is ready to use !

### Customize the design

You can [Customize Zinnia’s look and feel](http://docs.django-blog-zinnia.com/en/latest/how-to/customize_look_and_feel.html) or change the Zurb Foundation design [with Sass](http://foundation.zurb.com/docs/using-sass.html).

Icons are [Foundation Icon Fonts 3](http://zurb.com/playground/foundation-icon-fonts-3).

### Licence

Zinnia-theme-foundation is licensed under the [GNU GENERAL PUBLIC LICENSE version 3](http://www.gnu.org/licenses/gpl.txt).
