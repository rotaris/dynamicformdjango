from django.db import models

class List(models.Model):
    """A todo list"""
    name = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.name
    
    @models.permalink
    def get_absolute_url(self):
        return ('edit_items_in_list', (), {"pk": str(self.pk)})

class Item(models.Model):
    """A todo item to be done"""
    name = models.CharField("Item Name", max_length=150, help_text="e.g. Buy milk, wash dog etc")
    list = models.ForeignKey("List")
    
    def __unicode__(self):
        return "%s (%s)" % (self.name, str(self.list))
