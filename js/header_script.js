// JavaScript Document
jQuery(function(){
	var windowWidth = jQuery(window).width();
	if(windowWidth > 736){ 
		jQuery('#main_nav .parent').hover(function(){
			jQuery("ul:not(:animated)", this).slideDown();
			jQuery(this).addClass('se');
		}, function(){
			jQuery(".child",this).hide();
			jQuery(this).removeClass('se');
		});
	}else{
		jQuery("#main_nav, #main_nav .child").hide();
		

		jQuery("#main_nav .parent").on("click", function() {
			jQuery(this).children('ul').slideToggle();
			jQuery(this).toggleClass("open");
		});
		

		jQuery(".sidebar .sidebar_title").on("click", function() {
			jQuery('.sidebar ul').slideToggle();
			jQuery(this).toggleClass("open");
		});
		

		jQuery('#sp_nav').on("click", function() {
			jQuery('#sp_nav').toggleClass('open');
			jQuery('#main_nav').slideToggle();
		});
	}
	
});
