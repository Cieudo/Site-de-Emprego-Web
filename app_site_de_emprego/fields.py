from django.http import HttpResponse
from rlextra.rml2pdf import rml2pdf
import cStringIO

def getPDF(request):
    """Returns PDF as a binary stream."""

    # Use your favourite templating language here to create the RML string.
    # The generated document might depend on the web request parameters,
    # database lookups and so on - we'll leave that up to you.
    rml = getRML(request)  

    buf = cStringIO.StringIO()

    rml2pdf.go(rml, outputFileName=buf)
    buf.reset()
    pdfData = buf.read()

    response = HttpResponse(mimetype='application/pdf')
    response.write(pdfData)
    response['Content-Disposition'] = 'attachment; filename=output.pdf'
    return response