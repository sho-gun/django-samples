from django.views import generic
from django.http import HttpResponse
from django.urls import reverse_lazy
from file_upload.forms import FileUploadForm


class FileUploadSampleView(generic.FormView):
    template_name = 'upload_page.html'
    form_class = FileUploadForm
    success_url = reverse_lazy('file_upload:success_page')

    def form_valid(self, form):

        def is_ajax():
            """
            リクエストがAjaxを用いて送信されていたらTrue
            """
            return self.request.headers.get('x-requested-with') == 'XMLHttpRequest'

        # ファイルを保存
        file = form.cleaned_data['file']
        with open(f'{file.name}', 'wb+') as destination:
            if file.multiple_chunks():
                for chunk in file.chunks():
                    destination.write(chunk)
            else:
                destination.write(file.read())

        # AjaxによるPOSTの場合はリダイレクト先のURLをのものを返す
        if is_ajax():
            return HttpResponse(self.success_url)

        return super().form_valid(form)


class SuccessView(generic.TemplateView):
    template_name = 'success_page.html'
