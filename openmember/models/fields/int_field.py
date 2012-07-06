from openmember.models.field_adapter import FieldAdapter
from openmember.models.interfaces import IFieldAdapter
from openmember.models.interfaces import IFieldTemplate
from zope.interface.interface import Interface
import colander


class IntField(FieldAdapter):
    title = u"Integer Field"
    description = u"A numeric value"
    type_name = u"int_field"
    
    def get_node(self, context, request, name, title=u"", description = u"", **kw):
        node = colander.SchemaNode(colander.Int(), 
                                   name = name,
                                   title=title,
                                   description=description,
                                   **kw)
        return node
def includeme(config):
        config.registry.registerAdapter(IntField, (IFieldTemplate,), IFieldAdapter, name = IntField.type_name)
