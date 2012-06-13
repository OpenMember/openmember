import colander
from zope.interface import Interface

from openmember.models.field_adapter import FieldAdapter
from openmember.models.interfaces import IFieldAdapter


class StringField(FieldAdapter):
    title = u"String field"
    description = u"A short string"
    type_name = u"string_field"

    def get_node(self, context, request, name, title = u"", description = u"", **kw):
        node = colander.SchemaNode(colander.String(),
                                   name = name,
                                   title = title,
                                   description = description,
                                   **kw)
        return node


def includeme(config):
    config.registry.registerAdapter(StringField, (Interface,), IFieldAdapter, name = StringField.type_name)