from deform.exception import ValidationFailure
from deform.form import Form
from openmember.schemas.member_template import MemberSchema
from openmember.views.base import BaseView
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config


class CreateMemberView(BaseView):
    
    @view_config(name = 'create_member', renderer = 'templates/edit.pt')
    def create_member_view(self):
        schema = MemberSchema()
        schema = schema.bind(context = self.context, request = self.request)
        
        form = Form(schema, buttons = ('submit',))
        post = self.request.POST
        
        self.context.f_name = None
        self.context.m_name = None
        self.context.l_name = None
        self.context.birthdate = None
        
        response = {}
        response['form_resources'] = form.get_widget_resources(None)
        if 'submit' in post:
            controls = post.items()
            try:
                appstruct = form.validate(controls)
            except ValidationFailure, e:
                response['form'] = e.render()
                
            self.context.f_name = appstruct['f_name']
            self.context.m_name = appstruct['m_name']
            self.context.l_name = appstruct['l_name']
            self.context.birthdate = appstruct['birthdate']
            
        appstruct = dict(f_name = self.context.f_name, m_name = self.context.m_name, l_name = self.context.l_name, birthdate = self.context.birthdate)
        response['form'] = form.render(appstruct = appstruct)
        response['redirect'] = "//localhost/"
        if appstruct['f_name'] != None:
            return HTTPFound(location='http://eccentricrobot.com')
        return response