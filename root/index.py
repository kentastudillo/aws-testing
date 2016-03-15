import os
import json
import web

urls = (
    '/', 'index',
)

app = web.application(urls, globals())

web.config.session_parameters['timeout'] = 28800
web.config.session_parameters['expired_message'] = 'Session has expired. Please login.'

if web.config.get('_session') is None:
    session = web.session.Session(
        app,
        web.session.DiskStore('sessions'))
    web.config._session = session
else:
    session = web.config._session

# web.config.debug = True

render = web.template.render(
    'static/', base='base', globals={"session": session, 'json_encode': json.dumps})


class index:
    def GET(self):
        return 'hello world! this is my test site using aws! haha!'


if __name__ == "__main__":
    app.run()