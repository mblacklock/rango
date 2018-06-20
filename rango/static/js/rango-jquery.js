
$(document).ready(function() {
	// JQuery code here...
	console.log('JQuery initiated');
	
	$("#about-btn").click( function(event) {
		$(".p1").css('color', 'green');
		$("#p2").css('color', 'orange');
		
		msgstr = $("#msg").html()
		msgstr = msgstr + "ooo"
		$("#msg").html(msgstr)
		
	});
	
	$("p").hover( function() {
		$(this).css('color', 'red');
	},
	function() {
		$("p").css('color', 'blue');
	});
	
});