import cherrypy

class HelloSessionWorld(object):
    @cherrypy.tools.sessions()
    def index(self):
        if 'data' in cherrypy.session:
            return "App1. Voce esta logado! Usuario: %r" % cherrypy.session['data']
        else:
            return "App1. Voce nao esta logado. <a href='getcookie'>Entre</a>."
    index.exposed = True

    @cherrypy.tools.sessions()
    def getcookie(self):
        cherrypy.session['data'] = 'Maria'
        return "Pronto. Agora <a href='index'>retorne</a> para ver"
    getcookie.exposed = True

cherrypy.config.update({'server.socket_host': '0.0.0.0',
                        'server.socket_port': 8080,
                       })

application = cherrypy.tree.mount(HelloSessionWorld(), '/lb')

if __name__ == '__main__':
    cherrypy.quickstart(application)

