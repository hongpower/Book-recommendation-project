var form=$('.autocomplete-me')
var Autocomplete = function(options) {
  this.form_selector = options.form_selector
  this.url = form.url
  this.delay = parseInt(options.delay || 300)

  // 자동완성 기능 몇 글자부터 :
  this.minimum_length = parseInt(options.minimum_length || 2)

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
  this.query_box = this.form_elem.find('input[name=q]')

  // Watch the input box.
  this.query_box.on('keyup', function() {
    var query = self.query_box.val()

    if(query.length == 0){
      $('.ac-results').remove()  
    } else if (query.length < self.minimum_length) {
      return false
    }

    self.fetch(query)
  })

  // On selecting a result, populate the search field.
  this.form_elem.on('click', '.ac-result', function(ev) {
    self.query_box.val($(this).text())
    $('.ac-results').remove()
    return false
  })
}

Autocomplete.prototype.fetch = function(query) {
  var self = this
  $.ajax({
    //url: this.url
    url: '/auto_complete'
  , data: {
      'q': query
    }
  , success: function(data) {
      console.log(data)
      self.show_results(data)
    }
  })
}

Autocomplete.prototype.show_results = function(data) {
  // Remove any existing results.
  $('.ac-results').remove()

  var results = data.results || []
  var results_wrapper = $('<div class="ac-results"></div>')
  var base_elem = $('<div class="result-wrapper"><a href="#" class="ac-result"></a></div>')

  if(results.length > 0) {
    for(var res_offset in results) {
      var elem = base_elem.clone()
      // Don't use .html(...) here, as you open yourself to XSS.
      // Really, you should use some form of templating.
      elem.find('.ac-result').text(results[res_offset])
      results_wrapper.append(elem)
    }
  }
  else {
    var elem = base_elem.clone()
    elem.text("No results found.")
    results_wrapper.append(elem)
  }
  // 여기 수정:
  $(".autocomplete-me").append(results_wrapper)
  //$(".search-submit").after(results_wrapper)
  //this.query_box.after(results_wrapper)
}

$(document).ready(function() {
  window.autocomplete = new Autocomplete({
    form_selector: '.autocomplete-me'
  })
  window.autocomplete.setup()


})