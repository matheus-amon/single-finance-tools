from datetime import date

import streamlit as st
import requests

def calculate_share_rate(value, tax, calc):
	ngr = (value - (value*0.12)) * tax
	ggr = value * tax

	if calc == 'ggr':
		return ggr
	else:
		return ngr

@st.cache_data(ttl=60 * 60 * 24)
def get_exchange_rate(source, target, dt: date):
    url = f"https://api.exchangerate.host/{dt.isoformat()}"
    params = {"base": source, "symbols": target}

    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()
    data = r.json()

    if "rates" not in data or target not in data["rates"]:
        raise ValueError("Taxa de câmbio indisponível")

    return data["rates"][target]

def convert_currency(value, source, target, dt: date):
    if source == target:
        return value

    rate = get_exchange_rate(source, target, dt)
    return value * rate
