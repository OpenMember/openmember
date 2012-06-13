import colander
from repoze.folder import Folder
from zope.interface import implements
from BTrees.OOBTree import OOBTree

from openmember.models.interfaces import IContentTemplate


class ContentTemplate(Folder):
    implements(IContentTemplate)

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

    def get_schema(self, context, request, **kw):
        schema = colander.Schema()
        for fieldname in self.order:
            schema.add(self[fieldname].get_node(context, request, **kw))
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
