

# Create your views here.
# Code


def run(request):
    return "Res"



form_class = forms.SignUpForm
    success_url = reverse_lazy('hmg:recommended')
    template_name = 'hmg/signup.html'
