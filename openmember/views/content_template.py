from deform.exception import ValidationFailure
from deform.form import Form
from pyramid.request import Request
from pyramid.httpexceptions import HTTPFound
from pyramid.url import resource_url
from pyramid.view import view_config
from slugify import slugify

from openmember.models.field_template import FieldTemplate
from openmember.models.interfaces import IFieldAdapter
from openmember.models.interfaces import IContentTemplate
from openmember.schemas.content_template import ContentTemplateSchema
from openmember.views.base import BaseView


class ContentTemplate(BaseView):

    @view_config(context = IContentTemplate, renderer = 'templates/view.pt')
    def view(self):
        response = {}
        return response

    @view_config(name = "edit", context = IContentTemplate, renderer = 'templates/edit.pt')
    def edit(self):
        schema = ContentTemplateSchema()
        schema = schema.bind(context = self.context, request = self.request)
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
            
        appstruct = dict(title = self.context.title, description = self.context.description)
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
                self.data[slugify(ft.title)] = ft
                #data[slugify(ft.title)] = ft    #adds to the data array
                #results = ResultsView(self, self.context, self.request)
                #results.set_data(self.data)
            
            #url = resource_url(results, self.request)
            return HTTPFound(appstruct)
                
        return {'form':form.render(),'form_resources':form.get_widget_resources(None)}
