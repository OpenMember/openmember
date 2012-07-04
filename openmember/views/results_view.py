from deform.form import Form
from openmember.views.base import BaseView
from openmember.schemas.results_template import TextSchema
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
import colander
import csv

class ResultsView(BaseView):
    
    @view_config(name = 'temp', renderer = 'json')
    def try_import(self):
        csv_reader = csv.reader(open('/Users/Kaitlyn/Documents/Eccentric Robot/Dropbox/Kaitlyn/Betahaus/Open Member/open_member_test.csv', 'rU'), dialect=csv.excel)
        test_string = ""
        for row in csv_reader:
            test_string = test_string+' '.join(row)
        
        #process values in the rows to find the field names and titles
        
        return test_string
            
    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.data = None
        
    def set_data(self, data):
        self.data = data
        
            
    @view_config(name="results_page", renderer = 'templates/results.pt')
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
        schism = TextSchema().bind(type = ['turtle','peacock'])        
        form = Form(schism,button=('save',))
        #return HTTPFound(strDisp)
        return {'form':form.render(),'form_resources':form.get_widget_resources(None)}
