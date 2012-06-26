import colander
import deform

@colander.deferred
def deferred_choices_widget(node, kw):
    choices = kw.get('choices')
    return deform.widget.SelectWidget(values=choices)

class Field(colander.Schema):
    title = colander.SchemaNode(colander.String())
    description = colander.SchemaNode(colander.String())
    field_type = colander.SchemaNode(colander.String(), widget=deferred_choices_widget)

class Fields(colander.SequenceSchema):
    field = Field()


class ContentTemplateSchema(colander.Schema):
    fields = Fields()