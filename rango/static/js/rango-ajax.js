
$('#likes').click(function(){
	console.log("sdfjhskldf");
	var catid;
	catid = $(this).attr("data-catid");
	$.get('/rango/like/', {category_id: catid}, function(data){
		$('#like-count').html(data);
			$('#likes').hide();
	});
});

$('#suggestion').keyup(function(){
	console.log("suggestion");
	var query;
	query = $(this).val();
	console.log(query);
	$.get('/rango/suggest/', {suggestion: query}, function(data){
		$('#cats').html(data);
	});
});