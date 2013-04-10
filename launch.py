import cherrypy
from app import app
 
cherrypy.config.update({'server.socket_host': '0.0.0.0',
                        'server.socket_port': 8080})
cherrypy.tree.graft(app)
 
if __name__ == '__main__':
    try:
        cherrypy.engine.start()
    except KeyboardInterrupt:
        cherrypy.engine.stop()
