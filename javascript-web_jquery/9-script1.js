#!/usr/bin/node
$('document').ready(function () {
  $.ajax({
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    type: 'GET',
    crossDomain: true,
    jsonp: false,
    success: function (data, textStatus, jqXHR) {
      $('DIV#hello').text(data.hello);
    },
    error: function (jqXHR, textStatus, errorThrown) {
      console.log(`Here is the text status ${textStatus} and error ${errorThrown}`);
    }
  })
});
