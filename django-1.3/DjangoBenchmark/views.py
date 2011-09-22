from django.views.generic import TemplateView

class HelloWorldView(TemplateView):
    template_name = "hello_world.html"