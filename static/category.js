$(document).ready(function () {
  $.getJSON("http://localhost:8000/api/json_displaycategory", function (data) {
    $("#cid").append($("<option>").text("-Select Category-"));
    data.map((item) => {
      $("#cid").append(
        $("<option>").text(item.categoryname).val(item.id)
      );
    });
  });

  $("#cid").change(function () {
    $.getJSON("http://localhost:8000/api/jsondisplaysubcategory",{'cid':$('#cid').val()}, function (data) {
      $("#sid").empty()
      $("#sid").append($("<option>").text("-Select Brand-"));
      data.map((item) => {
        $("#sid").append(
          $("<option>").text(item.subcategoryname).val(item.id)
        );
      });
    });

  });

  $(function() {
    $( "#modelyear" ).datepicker();
});

  

  
});
