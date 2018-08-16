$(document).ready(function(){

		$("#id_shortcode").on('input',function(){
				var shortcode = this.value;
				var csrf      = $("[name='csrfmiddlewaretoken']").val();
				var toshow_error = $("#is_available");
				var shortcode_len   = shortcode.length; 

				$.ajax({
					type : 'POST',
					url  : '/shortcode/is_available/' ,

					data : {
						'shortcode' : shortcode,
						'csrfmiddlewaretoken' : csrf,
					},

					success : function(data){
						if(!data['is_available']){
							$(toshow_error).text('This url is already taken');
						}else{
							$(toshow_error).text('Available');
						}
					},

					error : function(data){
						console.log('Failing')
					},

				});
		});

	});
