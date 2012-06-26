from repoze.folder import Folder
from zope.interface import implements
from BTrees.OOBTree import OOBTree

from openmember.models.interfaces import IMembershipTerm


class MembershipTerm(Folder):
    implements(IMembershipTerm)

    def __init__(self):
        self._storage = OOBTree()
        super(MembershipTerm, self).__init__()

    def get_start_date(self):
        return self._storage.get('start_date', '')
    def set_start_date(self, value):
        self._storage['start_date'] = value
    start_date = property(get_start_date, set_start_date)

    def get_end_date(self):
        return self._storage.get('end_date', '')
    def set_end_date(self, value):
        self._storage['end_date'] = value
    end_date = property(get_end_date, set_end_date)
