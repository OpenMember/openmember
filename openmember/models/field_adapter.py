from zope.interface import implements

from openmember.models.interfaces import IFieldAdapter


class FieldAdapter(object):
    implements(IFieldAdapter)
    title = u""
    description = u""
    type_name = u""

    def __init__(self, context):
        self.context = context
