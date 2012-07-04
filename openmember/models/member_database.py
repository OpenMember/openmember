from repoze.folder import Folder
from zope.interface import implements

from openmember.models.interfaces import IMemberDatabase


class MemberDatabase(Folder):
    implements(IMemberDatabase)
    
        