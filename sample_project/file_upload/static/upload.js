$(() => {
  $('#submit-btn').on('click', () => {
    // multipart/form-dataでファイルをアップロードするための準備
    let myform = new FormData();
    myform.append('file', $('#upload_form').find('[name="file"]').prop('files')[0]);

    // アップロードボタンの無効化とプログレスバーの表示
    show_progress();
    disable_button();

    // Ajaxでアップロード
    $.ajax({
      type: 'POST',
      processData: false,
      contentType: false,
      headers: {
        'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').val()
      },
      data: myform,
      xhr : function(){
        // プログレスバーの更新
        var XHR = $.ajaxSettings.xhr();
        if(XHR.upload){
            XHR.upload.addEventListener('progress',function(e){
                var progress = parseInt(e.loaded/e.total*100);
                $('#progressbar').prop('aria-valuenow', progress);
                $('#progressbar').css('width', progress + '%');
            }, false);
        }
        return XHR;
      },
    })
    .done(data => {
      setTimeout(redirect, 1000, data);
    })
    .fail(data => {
      hide_progress();
      enable_button();
    });

    return false;
  });

  function show_progress() {
    $('#progressbar').prop('aria-valuenow', 0);
    $('#progressbar').css('width', '0%');
    $('#progress-container').removeAttr('hidden');
    $('#progress-container').show();
  }

  function hide_progress() {
    $('#progress-container').prop('hidden', true);
  }

  function disable_button() {
    $('#submit-btn').prop('disabled', true);
    $('#submit-btn-sm').prop('disabled', true);
  }

  function enable_button() {
    $('#submit-btn').removeAttr('disabled');
    $('#submit-btn-sm').removeAttr('disabled');
  }

  function redirect(url) {
    location.href = url;
  }

});
