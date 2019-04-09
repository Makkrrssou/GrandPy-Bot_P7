
$("form").submit(function(event){
	var extractVal=$("#extract").val();

	$("#message").append('<div class="client-side">'+extractVal+'</div>');
	$("#extract").val('');
	$("#chat_zone").scrollTop($('#chat_zone').prop("scrollHeight"));


	
	$.getJSON('/processing',{

		a:extractVal
	},function(data){

		$("#message").append('<iframe width="600" height="450" frameborder="0" style="border:0" src="https://www.google.com/maps/embed/v1/place?q='+extractVal+'&key={}" allowfullscreen></iframe> ');
		$("#message").append('<div class="server-side">'+data.result+'</div>');
		$("#chat_zone").scrollTop($('#chat_zone').prop("scrollHeight"));
	})
	.done(function(){
		console.log("ok!")
	})
	.fail(function(){
		alert("Votre message n'a pu être envoyé")
	});

	return false;

});

