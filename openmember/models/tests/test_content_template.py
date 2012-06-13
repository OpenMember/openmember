import unittest

from pyramid import testing
from zope.interface.verify import verifyClass
from zope.interface.verify import verifyObject

from openmember.models.interfaces import IContentTemplate


class ContentTemplateTests(unittest.TestCase):
    
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()
    
    @property
    def _cut(self):
        from openmember.models.content_template import ContentTemplate
        return ContentTemplate

    def test_verify_class(self):
        self.failUnless(verifyClass(IContentTemplate, self._cut))

    def test_verify_object(self):
        self.failUnless(verifyObject(IContentTemplate, self._cut()))

    def test_get_schema_with_string_field(self):
        self.config.include('openmember.register_fields')
        from openmember.models.field_template import FieldTemplate
        request = testing.DummyRequest()
        context = FieldTemplate() #Change to some other dummy context...
        obj = self._cut()
        obj['food'] = food = FieldTemplate()
        food.field_type = 'string_field'
        schema = obj.get_schema(context, request)
        self.assertEqual(schema.children[0].name, 'food')
