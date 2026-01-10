from datetime import date

import streamlit as st
from brutils.currency import format_currency

from utils.calculators import calculate_share_rate
from utils.exchange_rate_client import convert_currency

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

	with st.form('cc_form'):
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

		submitted = st.form_submit_button(
			'Calcular',
			on_click=convert_currency,
			kwargs={'value': value1, 'source': currency_source, 'target': currency_target, 'dt': date}
		)
