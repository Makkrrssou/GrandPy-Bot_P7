
$("form").submit(function(event){
	var extractVal=$("#extract").val();
	$("#extract").remove(extractVal);
	$("#message").append('<p class="client-side">'+extractVal+'</p>');

	
	$.getJSON('/processing',{

		a:extractVal
	},function(data){

		$("#message").append('<p class="server-side">'+data.result+'</p>');
		$("#message").append('<iframe width="600" height="450" frameborder="0" style="border:0" src="https://www.google.com/maps/embed/v1/place?q='+extractVal+'&key=AIzaSyD4oIexrzcN8LaIRaxszGHPMgRgPLCPxNE" allowfullscreen></iframe> ')
		
	})
	.done(function(){
		console.log("ok!")
	})
	.fail(function(){
		alert("Votre message n'a pu être envoyé")
	});

	return false;

});