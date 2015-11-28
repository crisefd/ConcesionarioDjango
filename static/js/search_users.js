//alert($('#searchTextInput').val())
var processSearch = function()  {
  var searchText = $('#searchTextInput').val().trim().toLowerCase();
 
  if(searchText.length < MIN_SEARCH_CHARS)  {
    //alert("pocos caracteres para buscar");
    //Too short. Ignore the submission, and erase any current results.
    $('#user_search_results').html("");
 
  } else  {
    //There are at least 4 characters. Execute the search.
 
    var processServerResponse = function(sersverResponse_data, 
                                        textStatus_ignored,
                                        jqXHR_ignored)  {
      /*alert("sersverResponse_data='" + sersverResponse_data + 
            "', textStatus_ignored='" + textStatus_ignored + 
            "', jqXHR_ignored='" + jqXHR_ignored + "'");*/
      $('#user_search_results').html(sersverResponse_data);
    }
 
    var config = {
      type: "GET",
      url: SUBMIT_URL,
      data: {
        'search_text' : searchText,
      },
      dataType: 'html',
      success: processServerResponse,
      async: true
    };
    $.ajax(config);
  }
};
var my_function = function(){alert("(((())))");};
var MILLS_TO_IGNORE_SEARCH = 100;

$(document).ready(function()  {
 $('#searchTextInput').keyup(
     
      _.debounce(processSearch,
      MILLS_TO_IGNORE_SEARCH, 
      true
      ));
});


 /*
 $(document).ready(function()  {
 $('#searchTextInput').keyup(
     console.log("keyed");
     );}
   );
*/