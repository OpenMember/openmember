from deform.exception import ValidationFailure
from deform.form import Form
from openmember.models.content_template import ContentTemplate
from openmember.models.field_template import FieldTemplate
from openmember.models.interfaces import IContentTemplate, IFieldAdapter, ISite
from openmember.models.interfaces import IMemberDatabase
from openmember.schemas.content_template import ContentTemplateSchema
from openmember.views.base import BaseView
from pyramid.httpexceptions import HTTPFound
from pyramid.request import Request
from pyramid.traversal import find_root
from pyramid.url import resource_url
from pyramid.view import view_config
from slugify import slugify


class ContentTemplateView(BaseView):
    
    
    def get_field_types(self):
        
        choices = set()
                
        for (name, plugin) in self.request.registry.getAdapters([self.context], IFieldAdapter):
            choices.add((name,plugin.title))
            
        return choices
        
    @view_config(name="add_page", context=IMemberDatabase, renderer = 'templates/edit.pt')
    def add(self):
        
        content_template = self.request.params.get('content_template')
        root = find_root(self.context)
        c_t_obj = root[content_template]
        schema = c_t_obj.get_schema(context = self.context, request = self.request)
        form = Form(schema, buttons=('save',))
        post = self.request.POST
        response = {}
        response['form_resources'] = form.get_widget_resources(None)
        if 'save' in post:
            controls = post.items()
            try:
                appstruct = form.validate(controls)
            except ValidationFailure, e:
                response['form'] = e.render()
                return response
            
            obj = ContentTemplate()
            obj.title = appstruct['title']
            obj.description = appstruct['description']
            obj.fields = appstruct['fields']
            #FIXME: Make adaptable to same titles
            self.context[slugify(obj.title)] = obj
            
            url = resource_url(obj, self.request)
            
            return HTTPFound(location=url)
        
        response['form'] = form.render()
        return response
    
#    @view_config(context = IContentTemplate, renderer = 'templates/view.pt')
    def view(self):
        response = {}
        return response

#    @view_config(name="edit_page", context=IContentTemplate, renderer = 'templates/edit.pt')
    def edit(self):
        schema = ContentTemplateSchema()
        schema = schema.bind(context = self.context, request = self.request, field_types = self.get_field_types())
        form = Form(schema, buttons=('save',))
        post = self.request.POST
        response = {}
        response['form_resources'] = form.get_widget_resources(None)
        if 'save' in post:
            controls = post.items()
            try:
                appstruct = form.validate(controls)
            except ValidationFailure, e:
                response['form'] = e.render()
                return response
            self.context.title = appstruct['title']
            self.context.description = appstruct['description']
            self.context.fields = appstruct['fields']
         
        appstruct = dict(title = self.context.title, description = self.context.description, fields = self.context.fields)
        response['form'] = form.render(appstruct = appstruct)
        return response
    
    def _fixme_edit(self):
        choices = set()
                
        for (name, plugin) in self.request.registry.getAdapters([self.context], IFieldAdapter):
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
                self.context[slugify(ft.title)] = ft
                #self.data[slugify(ft.title)] = ft
                #data[slugify(ft.title)] = ft    #adds to the data array
                #results = ResultsView(self, self.context, self.request)
                #results.set_data(self.data)
            
            #url = resource_url(results, self.request)
            return HTTPFound(appstruct)
                
        return {'form':form.render(),'form_resources':form.get_widget_resources(None)}
