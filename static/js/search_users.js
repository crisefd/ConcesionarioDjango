
var processSearch = function()  {
  var searchText = $('search_text').val().trim().toLowerCase();
 
  if(searchText.length < MIN_SEARCH_CHARS)  {
    //Too short. Ignore the submission, and erase any current results.
    $('#user_search_results').html("");
 
  }  else  {
    //There are at least two characters. Execute the search.
 
    var processServerResponse = function(sersverResponse_data, textStatus_ignored,
                        jqXHR_ignored)  {
      //alert("sersverResponse_data='" + sersverResponse_data + "', textStatus_ignored='" + textStatus_ignored + "', jqXHR_ignored='" + jqXHR_ignored + "'");
      $('#user_search_results').html(sersverResponse_data);
    }
 
    var config = {
      type: "GET",
      url: "/usuarios/busqueda",
      data: {
        'color_search_text' : searchText,
      },
      dataType: 'html',
      success: processServerResponse
    };
    $.ajax(config);
  }
};