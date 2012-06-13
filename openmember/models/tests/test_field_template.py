import unittest

from pyramid import testing
from zope.interface.verify import verifyClass
from zope.interface.verify import verifyObject

from openmember.models.interfaces import IFieldTemplate


class FieldTemplateTests(unittest.TestCase):
    
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()
    
    @property
    def _cut(self):
        from openmember.models.field_template import FieldTemplate
        return FieldTemplate

    def test_verify_class(self):
        self.failUnless(verifyClass(IFieldTemplate, self._cut))

    def test_verify_object(self):
        self.failUnless(verifyObject(IFieldTemplate, self._cut()))
