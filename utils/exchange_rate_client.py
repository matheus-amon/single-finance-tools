import os
from datetime import date

import httpx
from dotenv import load_dotenv
import asyncio

load_dotenv()
EXCHANGE_RATE_ACESS_KEY=os.getenv('EXCHANGE_RATE_ACESS_KEY')

client = httpx.AsyncClient(
	base_url='https://api.exchangerate.host/',
	headers={'Accept': 'application/json'},
	params={'access_key': EXCHANGE_RATE_ACESS_KEY}
)

def convert_currency(value, source, target, dt):
	response = asyncio.run(
		client.get(
			url='convert',
			params=[
				('from', source),
				('to', target),
				('amount', value),
				('date', dt)
			]
		)
	)
	result = response.json()
	result = result['result']
	return result
