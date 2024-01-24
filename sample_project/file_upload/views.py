from django.views import generic
from django.http import HttpResponse
from django.urls import reverse_lazy
from file_upload.forms import FileUploadForm


class FileUploadSampleView(generic.FormView):
    template_name = 'upload_page.html'
    form_class = FileUploadForm
    success_url = reverse_lazy('file_upload:success_page')

    def form_valid(self, form):
        """
        正常なファイルがアップロードされたときの処理
        """
        # ファイルを保存
        file = form.cleaned_data['file']
        with open(f'{file.name}', 'wb+') as destination:
            if file.multiple_chunks():
                for chunk in file.chunks():
                    destination.write(chunk)
            else:
                destination.write(file.read())

        # AjaxによるPOSTの場合はリダイレクト先のURLをのものを返す
        if self.__is_ajax():
            return HttpResponse(self.success_url)

        return super().form_valid(form)


    def form_invalid(self, form):
        """
        不正なファイルがアップロードされたときの処理
        例：0バイトのファイル
        """
        # AjaxによるPOSTの場合はリダイレクト先のURLをのものを返す
        if self.__is_ajax():
            return HttpResponse(reverse_lazy('file_upload:file_upload_sample'))

        return super().form_invalid(form)


    def __is_ajax(self):
        """
        リクエストがAjaxを用いて送信されていたらTrue
        """
        return self.request.headers.get('x-requested-with') == 'XMLHttpRequest'


class SuccessView(generic.TemplateView):
    template_name = 'success_page.html'
