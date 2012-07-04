import colander
import deform

@colander.deferred
def deferred_field_title(node, kw):
    return kw.get('type')[1]

def deferred_choices_widget(node, kw):
    type = kw.get('type')
    return deform.widget.TextInputWidget(size=60)
    
class TextBox(colander.Schema):
    content = colander.SchemaNode(
                                  colander.String(), 
                                  title = deferred_field_title, 
                                  description = deferred_field_title)
    
class TextSchema(colander.Schema):
    text_box = TextBox()
    #text_box.name_fields('turtle')
    
    