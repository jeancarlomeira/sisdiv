#middleware para carregar carrinho de compras sempre que usuario fizer login
#visto que a session muda a cada login
from .models import CartItem

def cart_item_middleware(get_response):
	def middleware(request):
		#antes do response
		#se a session_key antes da resposta for diferente da depois da resposta
		session_key = request.session.session_key
		response = get_response(request)
		#depois do response
		if session_key != request.session.session_key:
			CartItem.objects.filter(cart_key = session_key).update(cart_key = request.session.session_key)
		else:
			CartItem.objects.filter(cart_key = session_key)
		return response
	return middleware
