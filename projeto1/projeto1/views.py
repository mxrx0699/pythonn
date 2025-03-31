from django.http import HttpResponse
import socket
def home (request):
    # hostname = socket.gethostname()
    # message = f"Olá visitante de {hostname} - create by Mariana"
    message = ("<body bgcolor='pink'><h1>Mariana</h1></body>")
    return HttpResponse(message)