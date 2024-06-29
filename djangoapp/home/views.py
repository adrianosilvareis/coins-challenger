import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def index(request):
    return render(request, 'home/index.html')


def fetch_external_api_data(request):
    url = '{}/v1/cryptocurrency/quotes/latest'.format(
        settings.BASE_MARKETCAP_URL)

    symbols = request.GET.get('symbols', '')

    if not symbols:
        symbols = 'USDT,USDC,BTC'

    parameters = {
        'symbol': symbols
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': settings.API_KEY,
    }

    try:
        response = requests.get(url, headers=headers, params=parameters)
        response.raise_for_status()
        data = response.json()
        return render(request, 'home/index.html',
                      {'data': data['data'], 'symbols': symbols})
    except requests.exceptions.RequestException as e:
        return render(request, 'home/index.html',
                      {'error': str(e), 'symbols': symbols})
