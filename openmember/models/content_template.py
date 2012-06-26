import colander
from repoze.folder import Folder
from zope.interface import implements

from interfaces import IContentTemplate


class ContentTemplate(Folder):
    implements(IContentTemplate)
    
    title = None
    description = None
    
    def __init__(self):
        
        super(ContentTemplate, self).__init__()
        
    def get_schema(self, context, request, **kw):
        schema = colander.Schema()  #gets the current schema
        for fieldname in self.order:
            schema.add(self[fieldname].get_node(context, request, **kw))    #adds field subnode to the current schema
        schema.bind(context = context, request = request, **kw)
        return schema
        