from datetime import date

import requests
import streamlit as st
from brutils.currency import format_currency


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

col1, col2 = st.columns(2)

with col1:
	c1 = col1.container(border=True,)
	c1.markdown('### Calculadora de Share Rate')
	value = c1.number_input('Valor', 0.01, icon=':material/money:', key='sr_calc')
	tax = c1.number_input('Taxa', 0.1, 100.0, 10.0, 0.1,icon=':material/percent:') / 100
	calc = c1.selectbox('Indicador', ['GGR', 'NGR']).lower()
	result = format_currency(calculate_share_rate(value, tax, calc))
	c1.metric('Resultado', result, border=True)

with col2:
    c2 = col2.container(border=True)
    c2.markdown("### Conversão de Moedas")

    value1 = c2.number_input(
        "Valor",
        min_value=0.01,
        icon=":material/money:",
        key="cc_calc"
    )

    ccol1, ccol2 = c2.columns(2)
    currency_source = ccol1.selectbox("Da moeda:", ["EUR", "BRL", "USD"])
    currency_target = ccol2.selectbox("Para:", ["EUR", "BRL", "USD"])
    date = c2.date_input("Data de cotação")

    try:
        result = convert_currency(
            value1,
            currency_source,
            currency_target,
            date
        )
        c2.metric("Resultado", format_currency(result), border=True)
    except Exception as e:
        c2.error(str(e))
