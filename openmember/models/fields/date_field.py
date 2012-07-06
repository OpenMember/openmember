from openmember.models.field_adapter import FieldAdapter
from openmember.models.interfaces import IFieldAdapter
from openmember.models.interfaces import IFieldTemplate
from zope.interface.interface import Interface
import colander


class DateField(FieldAdapter):
    title = u"Date Field"
    description = u"A date value"
    type_name = u"date_field"
    
    def get_node(self, context, request, name, title=u"", description = u"", **kw):
        node = colander.SchemaNode(colander.Date(), 
                                   name = name,
                                   title=title,
                                   description=description,
                                   **kw)
        return node
    
def includeme(config):
        config.registry.registerAdapter(DateField, (IFieldTemplate,), IFieldAdapter, name = DateField.type_name)
