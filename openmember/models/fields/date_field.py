from openmember.models.field_adapter import FieldAdapter
from openmember.models.interfaces import IFieldAdapter
from openmember.models.interfaces import IContentTemplate
from zope.interface.interface import Interface
import colander


class DateField(FieldAdapter):
    title = u"Date Field"
    description = u"A date value"
    type_name = u"date_field"
    
    def get_node(self, context, request, name, title=u"", description = u"", **kw):
        node = colander.SchemaNode(colander.Int(), 
                                   name = name,
                                   title=title,
                                   description=description,
                                   **kw)
        return node
    
def includeme(config):
        config.registry.registerAdapter(DateField, (IContentTemplate,), IFieldAdapter, name = DateField.type_name)
