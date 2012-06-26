from zope.interface import Attribute
from zope.interface import Interface


class IMemberDatabase(Interface):
    """ """


class IMembershipTerm(Interface):
    """ """
    start_date = Attribute("Start date")
    end_date = Attribute("Start date")


class IMemberData(Interface):
    """ Contains data on a specific member.
        Created from a ContentTemplate.
    """
    content_type = Attribute("Which content type this data is based on. Must be equal to an existing ContentTemplate name")

    def get(key, default = None):
        """  """

    def set(key, value):
        """ """

    def update(values):
        """ Set several values at once. Usually a returned appstruct dict that comes from deform.
            Must be in dict format and each key must correspond to an actual field.
        """


class IContentTemplate(Interface):
    """ Content type information """
    title = Attribute("Title of this content type")
    description = Attribute("Informative description")
    order = Attribute("field order")

    def get_schema(context, request, **kw):
        """ Return an instanciated schema with context and request + any kw bound. """

    def member_data_factory(values):
        """ Return a member data object. Values must be a dict, where each key is a corresponding existing field.
            FIXME: This is where we'll preform the "soft" validation later on, to mark things as problematic. If this is the right way to go that is :)
        """

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
