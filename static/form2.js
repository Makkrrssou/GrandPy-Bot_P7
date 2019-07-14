
$("form").submit(function(event){
	var extractVal=$("#extract").val();

	$("#message").append('<div class="client-side">'+extractVal+'</div>');
	$("#extract").val('');
	$("#chat_zone").scrollTop($('#chat_zone').prop("scrollHeight"));


	
	$.getJSON('/processing',{

		a:extractVal
	},function(data){

		var results=data.result;
		var dic_result=results.split(';');
		$("#message").append('<div class="server-side">'+dic_result[1]+'</div>');
		$("#message").append('<div class="server-side">'+dic_result[0]+'</div>');
		$("#chat_zone").scrollTop($('#chat_zone').prop("scrollHeight"));
	})
	.done(function(){
		console.log("ok!");
	})
	.fail(function(){
		alert("Votre message n'a pu être envoyé");

	});

	
	
	var map;
	$("#message").append('<div id=map></div>');
	function initMap() {
		map = new google.maps.Map(document.getElementById('map'), {
		center: {lat: -34.397, lng: 150.644},
		zoom: 8
		});
	}

	return false;	

});

