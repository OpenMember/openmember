import unittest

from pyramid import testing
from zope.interface.verify import verifyClass
from zope.interface.verify import verifyObject
from zope.interface import Interface
from zope.interface import implements

from openmember.models.interfaces import IFieldAdapter


class StringFieldTests(unittest.TestCase):
    
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()
    
    @property
    def _cut(self):
        from openmember.models.fields.string_field import StringField
        return StringField

    def test_verify_class(self):
        self.failUnless(verifyClass(IFieldAdapter, self._cut))

    def test_verify_object(self):
        self.failUnless(verifyObject(IFieldAdapter, self._cut(None)))

    def test_integration(self):
        from openmember.models.field_template import FieldTemplate
        self.config.include('openmember.models.fields.string_field')
        context = FieldTemplate()
        self.failUnless(self.config.registry.queryAdapter(context, IFieldAdapter, self._cut.type_name))

