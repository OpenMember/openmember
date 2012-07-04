from BTrees.OOBTree import OOBTree
from interfaces import IContentTemplate
from openmember.models.interfaces import IFieldAdapter
from repoze.folder import Folder
from zope.component._api import getAdapter
from zope.interface import implements
import colander
import slugify



class ContentTemplate(Folder):
    implements(IContentTemplate)    
    title = None
    description = None
    fields = None
    
    def __init__(self):
        self._storage = OOBTree()
        super(ContentTemplate, self).__init__()

    def get_title(self):
        return self._storage.get('title', '')
    def set_title(self, value):
        self._storage['title'] = value
    title = property(get_title, set_title)

    def get_description(self):
        return self._storage.get('description', '')
    def set_description(self, value):
        self._storage['description'] = value
    description = property(get_description, set_description)
    
    def get_fields(self):
        return self._storage.get('fields', ())
    def set_fields(self, value):
        if not isinstance(value, tuple):
            value = tuple(value)
        self._storage['fields'] = value
    fields = property(get_fields, set_fields)

    def get_schema(self, context, request, **kw):
        schema = colander.Schema()  #gets the current schema
        for field in self.get_fields():
            adapter = getAdapter(self, name = field['field_type'], interface = IFieldAdapter)
            schema.add(adapter.get_node(context, request, name = slugify(field['title']), title = field['title'], description = field['description'], **kw))    #adds field subnode to the current schema
        schema.bind(context = context, request = request, **kw)
        return schema

    def member_data_factory(self, values):
        #XXX This is an example
        #FIXME: Add factories later on
        from openmember.models.member_data import MemberData
        #FIXME: Soft validation goes here, i.e check if data contains errors or problems, but don't die on errors
        #Check that fields actually exist
        for k in values:
            if k not in self:
                raise KeyError("There's no field with name '%s' in %s" % (k, self))
        return MemberData(values)
