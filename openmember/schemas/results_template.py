import colander
import deform

def deferred_choices_widget(node, kw):
    type = kw.get('type')
    return deform.widget.TextInputWidget(size=60)
    
class TextBox(colander.Schema):
    title = colander.SchemaNode(colander.String())
    dontent = colander.SchemaNode(colander.String())
    
class TextSchema(colander.Schema):
    text_box = TextBox()
    
    