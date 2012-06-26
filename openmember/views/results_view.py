from deform.form import Form
from openmember.schemas.results_template import TextSchema
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
import colander

class ResultsView(object):
    
    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.data = None
        
    def set_data(self, data):
        self.data = data
        
            
    @view_config(renderer = 'templates/results.pt')
    def render_results_view(self):
        strDisp = ""
        if self.data is not None:
            for field in self.data:
                #Allows for concatenation for display
                title = field['title']
                description = field['description']
                field_type = field['field_type']
                
                #concatenating the data
                strDisp = strDisp.concatenate(' %s %s %s ' % (title, description, field_type))
            
        #temporary schema to see if the results are being transferred
        schism = TextSchema()        
        form = Form(schism,button=('submit',))
        #return HTTPFound(strDisp)
        return {'form':form.render(),'form_resources':form.get_widget_resources(None)}
