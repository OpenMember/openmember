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
