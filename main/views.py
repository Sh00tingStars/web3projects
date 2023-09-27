from django.shortcuts import render
from web3 import Web3
def home(request):
    return render(request, 'home.html')




def login_with_metamask(request):
    if request.method == 'POST':
        # Обработка POST-запроса (если это необходимо)
        pass
    else:
        # Если пользователь уже авторизован через MetaMask, получите его Ethereum-адрес
        user_address = None
        if 'web3' in request:
            web3 = Web3(request.web3.currentProvider)
            if web3.isConnected():
                user_accounts = web3.eth.accounts
                if user_accounts:
                    user_address = user_accounts[0]

        # Отправьте адрес пользователя в шаблон
        return render(request, 'login_with_metamask.html', {'user_address': user_address})


def profile(request):
    return render(request, 'profile.html')

