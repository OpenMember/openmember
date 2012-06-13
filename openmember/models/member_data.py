from repoze.folder import Folder
from zope.interface import implements
from BTrees.OOBTree import OOBTree

from openmember.models.interfaces import IMemberData


class MemberData(Folder):
    implements(IMemberData)

    def __init__(self, content_type, values):
        self.content_type = content_type
        super(MemberData, self).__init__()
        self._storage = OOBTree()
        if data:
            self.update(values)

    def get(self, key, default = None):
        return self._storage.get(key, default)

    def set(self, key, value):
        #FIXME: Validation here?
        self._storage[key] = value

    def update(self, values):
        for (k, v) in values.items():
            self.set(k, v)
