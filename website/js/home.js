function main() {
  $('.explanation').hide();
  
  $('.btn-default').on('click', function() {
	$(this).next().slideToggle(400);
    $(this).toggleClass('active');
	});
}

$(document).ready(main);