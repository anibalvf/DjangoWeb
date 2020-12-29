
class AddLoQueSeaMixin(object):
    def get_context_data(self,**kwargs):
        context= super().get_context_data(**kwargs)
        context['algo']= "Ramon el vanidoso"
        return context