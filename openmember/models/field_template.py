from BTrees.OOBTree import OOBTree
from openmember.models.interfaces import IFieldAdapter, IFieldTemplate
from repoze.folder import Folder
from zope.interface import implements
import pdb



class FieldTemplate(Folder):
    """ Field information """
    implements(IFieldTemplate)

    def __init__(self, title=u"", description=u"", field_type=u""):
        self._storage = OOBTree()
        super(FieldTemplate, self).__init__()
        self.title = title
        self.description = description
        self.field_type = field_type

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

    def get_field_type(self):
        return self._storage.get('field_type', '')
    def set_field_type(self, value):
        self._storage['field_type'] = value
    field_type = property(get_field_type, set_field_type)

    def get_node(self, context, request, name = None, **kw):
        if name is None:
            name = self.__name__
        fa = request.registry.getAdapter(self, IFieldAdapter, name = self.field_type)
        return fa.get_node(context, request, name, title = self.title,
                           description = self.description, **kw)

