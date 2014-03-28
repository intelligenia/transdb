OVERVIEW

Django's field that stores labels in more than one language in database.

AUTHOR

This package was created by msaelices@gmail.com and was hosted in
https://code.google.com/p/transdb/ but in recent versions of
Django (1.5 and later) stopped working.

intelligenia has made a branch with the aim of supporting a up-to-date
version of this package.

INSTALLATION

See Installation file in this directory.

USAGE

Create your models:

    from transdb import TransCharField, TransTextField
    [...]

    class MyModel(models.Model):
        [...]
        my_char_field = TransCharField(max_length=32)
        my_text_field = TransTextField()

If you need to use in models in a more advanced way:

    from transdb import TransDbField
    from django.conf import settings
    from django.utils.translation import get_language
    from django.template.defaultfilters import slugify
    [...]

    class MyModel(models.Model):
        [...]
        my_char_field = TransCharField(max_length=32)
        my_text_field = TransTextField()
        slug_field = models.SlugField(editable=False)

        def __unicode__(self):
            return self.my_char_field

        def save(self):
            self.slug_field = slugify(self.my_char_field.get_in_language(settings.LANGUAGE_CODE))
            super(MyModel, self).save()
    [...]

Use as any other field in templates:

    [...]
    <p>{{ object.my_field }}</p>
    [...]

And that's all, enjoy!

MIGRATION

Migration from non-translatable fields (and previous versions of TransDb)

There is a wiki page that covers the migration procedure from non-translatable fields:

    http://code.google.com/p/transdb/wiki/MigrationProcedure

TECHINCAL INFORMATION

Internally data is stored in database as a string in dictionary format, for example:

    u'{u'en': u'This is english', u'es': u'Esto es español'}'

Field uses a subclass of unicode class, adding a raw_data attribute to store the string with all languages, and implementing the get_in_language(language) method to allow access to a diferent language (diferent from the user's current language).

KNOWN ISSUES

See the list in http://code.google.com/p/transdb/issues/list 
