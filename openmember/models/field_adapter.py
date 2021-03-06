from zope.interface import implements

from openmember.models.interfaces import IFieldAdapter
from openmember.models.interfaces import IGroupingAdapter


class FieldAdapter(object):
    implements(IFieldAdapter)
    title = u""
    description = u""
    type_name = u""

    def __init__(self, context):
        self.context = context

class NewAdapter(FieldAdapter):
    
    def __init__(self, context):
        self.context = context
        self.title = u"new adapter"
        self.description = u"a new type of field adapter"
        self.type_name = u"tba"
        
class GroupingAdapter(object):
    implements(IGroupingAdapter)
    
    fields = set()
    
    def __init__(self, context):
        self.context = context
        
    