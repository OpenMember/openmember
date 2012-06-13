from zope.interface import Attribute
from zope.interface import Interface


class IMemberDatabase(Interface):
    """ """


class IContentTemplate(Interface):
    """ Content type information """
    title = Attribute("Title of this content type")
    description = Attribute("Informative description")
    order = Attribute("field order")

    def get_schema(context, request, **kw):
        """ Return an instanciated schema with context and request + any kw bound. """


class IFieldTemplate(Interface):
    """ Contains information on a field type. """
    title = Attribute("Title of this field")
    description = Attribute("Informative description")
    field_type = Attribute("Which type of field this is. Used to look up a field adapter.")

    def get_node(context, request, **kw):
        """ Return a colander.SchemaNode """


class IFieldAdapter(Interface):
    """ Knows how to handle fields """
    title = Attribute("Title of the adapter type")
    description = Attribute("Description of this type")
    type_name = Attribute("Name of the adapter type. Must be unique")

    def get_node(context, request, name, title = u"", description = u"", **kw):
        """ Return a colander.SchemaNode """
