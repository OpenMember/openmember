import colander
import deform

@colander.deferred
def deferred_choices_widget(node, kw):
    choices = kw.get('field_types',())
    return deform.widget.SelectWidget(values=choices)

class FieldTemplateSchema(colander.Schema):
    title = colander.SchemaNode(colander.String())
    description = colander.SchemaNode(colander.String())
    field_type = colander.SchemaNode(colander.String(), widget=deferred_choices_widget)


class ContentTemplateSchema(colander.Schema):
    title = colander.SchemaNode(colander.String())
    description = colander.SchemaNode(colander.String())
