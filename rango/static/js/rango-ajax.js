
$('#likes').click(function(){
	console.log("sdfjhskldf");
	var catid;
	catid = $(this).attr("data-catid");
	$.get('/rango/like/', {category_id: catid}, function(data){
		$('#like-count').html(data);
			$('#likes').hide();
	});
});