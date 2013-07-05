from django.db import models
from django.utils.translation \
    import ugettext_lazy as _
from django.core.urlresolvers import \
    reverse

# Create your models here.
from ..core.models import TimeStampedModel


class MyModel(TimeStampedModel):
    """
    Just example of model
    """
    title = models.CharField(
        _('Title'),
        max_length=200
    )

    def get_absolute_url(self):
        return reverse('mymodel:detail',
                       args=[self.pk])

    def __unicode__(self):
        return self.title
