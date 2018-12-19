$(document).ready(function() {

	$("#submit").on('submit', function(event) {

		$.ajax({
			data : {
				response : $("#extract").val(),
			},
			type : 'POST',
			url : '/processing'
			
		})
		.done(function(data) {

			
			$("#chat_zone").write(data.response);
			
		});

		event.preventDefault();

	});

});