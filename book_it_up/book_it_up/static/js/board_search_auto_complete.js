var form=$('.board-autocomplete-me')
var Autocomplete = function(options) {
  this.form_selector = options.form_selector
  this.url = form.url
  this.delay = parseInt(options.delay || 300)

  // 자동완성 기능 몇 글자부터 :
  this.minimum_length = parseInt(options.minimum_length || 1)

  this.form_elem = null
  this.query_box = null
}

    $.ajaxSetup({
    beforeSend: function (xhr, settings) {
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';')
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i])
                    // Does this cookie string begin with the name we want?-->
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.-->
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
})

Autocomplete.prototype.setup = function() {
  var self = this

  this.form_elem = $(this.form_selector)
  this.query_box = this.form_elem.find('input[id="id_query"]')

  // Watch the input box.
  this.query_box.on('keyup', function() {
    var query = self.query_box.val()

    if(query.length == 0){
      $('.board-ac-results').remove()
    } else if (query.length < self.minimum_length) {
      return false
    }

    self.fetch(query)
  })

  // On selecting a result, populate the search field.
  this.form_elem.on('click', '.board-ac-result', function(ev) {

    // display를 보여준다
    $("article:nth-child(2)").css('display', 'block')
   //self.query_box.val($(this).find('div:nth-child(3)').text())
    $("#book-id").val($(this).find('div:nth-child(3)').text())
    var imgSrc = $(this).find('div:nth-child(1)').find('img').prop('src')
    var bookImg = "<img src=" + imgSrc + ">"
    var bookTitle = $(this).find('div:nth-child(2)').text()
    $(".book-small-img-container").find('img').remove()
    $(".book-small-img-container").append(bookImg)
    $("#book-title").val('')
    $("#book-title").val(bookTitle)
    $('.board-ac-results').remove()

    return false
  })
}

Autocomplete.prototype.fetch = function(query) {
  var self = this
  $.ajax({
    //url: this.url
    url: '/board/auto_complete'
  , data: {
      'q': query
    }
  , success: function(data) {
      self.show_results(data)
    }
  })
}

Autocomplete.prototype.show_results = function(data) {
  // Remove any existing results.
  $('.board-ac-results').remove()

  var results = data.results || []
  var results_wrapper = $('<div class="board-ac-results"></div>')
  var base_elem = $('<div class="board-result-wrapper"><a href="#" class="board-ac-result"></a></div>')

  if (results.length > 0){
    for (i in results){
        var book = results[i]
        var elem = base_elem.clone()
        for (j in book){
            if(j==0){
                 elem.find('.board-ac-result').append("<div><img src='"+book[j]+"'></div>")
                results_wrapper.append(elem)
            } else {
                elem.find('.board-ac-result').append("<div>"+book[j]+"</div>")
                results_wrapper.append(elem)
            }
        }
    }
  } else {
    var elem = base_elem.clone()
    elem.text("해당 도서가 없습니다.")
    results_wrapper.append(elem)
  }

  // 여기 수정:
  $(".board-autocomplete-me").append(results_wrapper)
  //$(".search-submit").after(results_wrapper)
  //this.query_box.after(results_wrapper)
}

$(document).ready(function() {
  window.autocomplete = new Autocomplete({
    form_selector: '.board-autocomplete-me'
  })
  window.autocomplete.setup()


})