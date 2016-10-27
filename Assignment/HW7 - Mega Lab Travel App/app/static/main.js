
  $("#tripdata").on('click', "a", function() {

		//delete item
    var id = this.closest("tr").id;
		console.log("removing from list");
		$(this.closest("tr")).remove();

    $.ajax({
      url: '/ajax_delete',
      data: {'id': id},
      type: "POST",
      success: function(result) {
                console.log(result);
            }
    });

});
