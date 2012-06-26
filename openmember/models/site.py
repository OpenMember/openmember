from repoze.folder import Folder
from zope.interface import implements

from openmember.models.interfaces import ISite


class SiteRoot(Folder):
    """ Site root """
    implements(ISite)
