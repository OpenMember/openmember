from deform.exception import ValidationFailure
from deform.form import Form
from pyramid.config import Configurator
from pyramid_zodbconn import get_connection
from wsgiref.simple_server import make_server
import colander


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(root_factory=root_factory, settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_static_view('deform', 'deform:static')
    
    
    
    config.include(register_fields)
    config.scan()
    return config.make_wsgi_app()

def root_factory(request):
    conn = get_connection(request)
    return appmaker(conn.root())

def appmaker(zodb_root):
    if not 'app_root' in zodb_root:
        from openmember.models.site import SiteRoot
        app_root = SiteRoot()
        zodb_root['app_root'] = app_root
        app_root['example'] = initial_content()
        import transaction
        transaction.commit()
    return zodb_root['app_root']

def initial_content():
    from openmember.models.member_database import MemberDatabase
    from openmember.models.content_template import ContentTemplate
    from openmember.models.field_template import FieldTemplate
    obj = MemberDatabase()
    obj['person'] = person = ContentTemplate()
    person['first_name'] = FieldTemplate(title = u"First name",
                                         field_type = u"string_field")
    
    #FIXME: Setup admin account etc
    return obj

def register_fields(config):
    config.include('openmember.models.fields.string_field')
    config.include('openmember.models.fields.int_field')
    config.include('openmember.models.fields.date_field')

