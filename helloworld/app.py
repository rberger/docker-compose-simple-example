from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import consul

c = consul.Consul(host='consul')
c.kv.put('mykey', 'myvalue')

def hello_world(request):
    print('Incoming request')
    index, data = c.kv.get('mykey')
    str = '{0} value: {1}'.format(data["Key"], data["Value"])
    return Response('<body><h1>Hello World!<br>' + str + '</h1></body>')

if __name__ == '__main__':
    config = Configurator()
    config.add_route('hello', '/')
    config.add_view(hello_world, route_name='hello')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 5000, app)
    server.serve_forever()

