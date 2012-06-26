from deform import schema
from deform.exception import ValidationFailure
from deform.form import Form
from openmember.models.field_adapter import FieldAdapter
from openmember.models.field_template import FieldTemplate
from openmember.models.interfaces import IFieldAdapter
from openmember.schemas.content_template import ContentTemplateSchema
from pyramid.request import Request
from pyramid.httpexceptions import HTTPFound
from pyramid.url import resource_url
from pyramid.view import view_config
#from results_view import ResultsView
from slugify import slugify
#from arrays import *

class BaseView(object):

    def __init__(self, context, request):
        self.context = context
        self.request = request

    @view_config(renderer = 'templates/base.pt')
    def view(self):
        choices = set()
        
        fake_poll = FieldAdapter(self.context)
        
        for (name, plugin) in self.request.registry.getAdapters([fake_poll], IFieldAdapter):
            choices.add((name,plugin.title))
            
        conTemp = ContentTemplateSchema().bind(choices=choices)
        form = Form(conTemp,buttons=('submit',))
        post = self.request.POST
        if 'submit' in post:
            controls = post.items()
            try:
                appstruct = form.validate(controls)
            except ValidationFailure, e:
                return {'form':e.render(),'form_resources':e.get_widget_resources(None)}
            self.data = {}
            
            for field in appstruct['fields']:
                ft = FieldTemplate()
                ft.title = field['title']
                ft.description = field['description']
                ft.field_type = field['field_type']
                self.data[slugify(ft.title)] = ft
                #data[slugify(ft.title)] = ft    #adds to the data array
                #results = ResultsView(self, self.context, self.request)
                #results.set_data(self.data)
            
            #url = resource_url(results, self.request)
            return HTTPFound(appstruct)
                
        return {'form':form.render(),'form_resources':form.get_widget_resources(None)}
