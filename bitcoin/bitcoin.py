import sys
import requests

def main():
    if len(sys.argv) < 2:
        sys.exit('Missing command-line argument')

    try:
        number = float(sys.argv[1])

        r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

        bit_rate = r.json()['bpi']['USD']['rate_float']

        bit_in_dol = number * bit_rate

        print(f"${bit_in_dol:,.4f}")

    except ValueError:
        sys.exit('Command-line argument is not a number')
    except requests.RequestException:
        sys.exit('API error')

main()