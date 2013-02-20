import web
import time
import httplib2
import httplib

urls = ('/upload', 'Upload')

class Upload:
    def GET(self):
        web.header("Content-Type","text/html; charset=utf-8")
        return """<html><head></head><body>
<form method="POST" enctype="multipart/form-data" action="">
<input type="file" name="myfile" />
<br/>
<input type="submit" />
</form>
</body></html>"""

    def POST(self):
        file_size = web.utils.intget(web.ctx.env.get('CONTENT_LENGTH'), 0) 
        filename = str(time.time())
        h2 = httplib.HTTPConnection("192.168.5.11:9500")
        h2.putrequest("POST", "/api/upload/"+filename)
        h2.putheader('Content-Type', 'multipart/form-data')
        h2.putheader('Content-Length', file_size)
        h2.endheaders()
        step = 1024*1024*10
        while 0<file_size:
            if file_size - step <= 0:
                step = file_size
            data = web.ctx.env['wsgi.input'].read(step)
            h2.send(data)
            file_size = file_size - step
        print '*'*100, filename
        r2 = h2.getresponse()
        print r2.status, r2.reason, r2.read()
        h2.close()

if __name__ == "__main__":
   app = web.application(urls, globals()) 
   app.run()
