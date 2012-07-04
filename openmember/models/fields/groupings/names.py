from openmember.models.fields.string_field import StringField
from openmember.models.fields.date_field import DateField

from openmember.models import fields
from openmember.models.field_adapter import GroupingAdapter

class NameFieldGrouping(GroupingAdapter):
    def __init__(self, context):
        
        self.context = context
        
        fields['f_name'] = {'first name':StringField(self.context)}
        fields['m_name'] = {'middle name':StringField(self.context)}
        fields['l_name'] = {'last name':StringField(self.context)}
        fields['birthdate'] = {'birthdate':DateField(self.context)}
        
    def get_node(self, context, request, name, title = u"", description = u"", **kw):
        
        schemas = {}
        
        for field in fields:
            schemas[field.name] = field.get_node(field, self.context, 
                           request, field.name, field.title, 
                           field.description, **kw)
    
