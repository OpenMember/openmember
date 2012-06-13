import colander
from repoze.folder import Folder
from zope.interface import implements

from openmember.models.interfaces import IContentTemplate


class ContentTemplate(Folder):
    implements(IContentTemplate)
    
    title = None
    description = None

    def get_schema(self, context, request, **kw):
        schema = colander.Schema()
        for fieldname in self.order:
            schema.add(self[fieldname].get_node(context, request, **kw))
        schema.bind(context = context, request = request, **kw)
        return schema
