import morepath
import webob
from webob.exc import HTTPNotFound
from webob.static import DirectoryApp, FileApp
from .app import App


def run():   # pragma: no cover
    morepath.autoscan()

    index = FileApp('static/index.html')
    static = DirectoryApp('static')
    app = App()

    @webob.dec.wsgify
    def morepath_with_static(request):
        if request.path_info_peek() == '':
            return request.get_response(index)

        popped = request.path_info_pop()
        if popped == 'api':
            return request.get_response(app)
        elif popped == 'static':
            return request.get_response(static)

        raise HTTPNotFound()

    morepath.run(morepath_with_static)
