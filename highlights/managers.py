from django.db import models



class HighlightQuerySet(models.query.QuerySet):
    def live(self):
        return self.filter(status__gte=2)

class PublicManager(models.Manager):
    """Returns published featured teasers."""
    
    use_for_related_fields = True
    
    def get_query_set(self):
        return HighlightQuerySet(self.model)
        
    def live(self, *args, **kwargs):
        return self.get_query_set().live(*args, **kwargs)