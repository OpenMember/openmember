from pyramid.view import view_config


class BaseView(object):

    def __init__(self, context, request):
        self.context = context
        self.request = request

    @view_config(renderer = 'templates/base.pt')
    def view(self):
        return {}
