from django.db import models
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail import ImageField
from django.db.models import permalink

from managers import PublicManager


class HighlightGroup(models.Model):
    name = models.CharField(_("name"), max_length=50, unique=True)
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = u'HighlightGroup'
        verbose_name_plural = 'HighlightGroups'
    
    def __unicode__(self):
        return self.name
        
class Highlight(models.Model):
    """
    (Featured description)
    """
    STATUS_CHOICES = (
        (0, _('Private')),
        (1, _('Draft')),
        (2, _('Public')),
    )
    highlight_group = models.ForeignKey(HighlightGroup, related_name="highlights")
    title = models.CharField(max_length=150)
    slug = models.SlugField()
    caption = models.CharField(_('caption'), blank=True, max_length=255)
    excerpt = models.TextField(blank=True)
    description = models.TextField(_('description'))
    
    image  = ImageField(_('picture'), upload_to='highlights', blank=True)
    link    = models.URLField(blank=True)
    text_button = models.CharField(_('Text button'), default="Read More", max_length=50)
    status  = models.IntegerField(_('status'), choices=STATUS_CHOICES, default=2)
    # position field
    position = models.PositiveSmallIntegerField("Position", default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = PublicManager()
    
    class Meta:
        verbose_name = u'Highlight'
        verbose_name_plural = 'Highlights'
        ordering = ('position',)
    
    def __unicode__(self):
        return self.title
