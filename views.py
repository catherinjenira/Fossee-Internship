from django.http import HttpResponse


def index(request):
    html = """
    <html>
      <head>
        <title>Chemical Visualizer</title>
      </head>
      <body style="background:#1a001a;color:#e6ccff;font-family:Arial;">
        <h1>Chemical Visualizer — Backend</h1>
        <p>API available at <a href="/api/">/api/</a></p>
        <p>If you're developing the frontend, run your React app (usually on <code>http://localhost:3000</code>).</p>
      </body>
    </html>
    """
    return HttpResponse(html)


def favicon(request):
    # Return 204 No Content so browsers don't log a 404 for favicon
    return HttpResponse(status=204)
