import streamlit as st
from brutils.currency import format_currency


def calculate_share_rate(value, tax, calc):
	ngr = (value - (value*0.12)) * tax
	ggr = value * tax

	if calc == 'ggr':
		return ggr
	else:
		return ngr

col1, col2 = st.columns(2)

c = col1.container(border=True, )
c.markdown('### Calculadora de Share Rate')
value = c.number_input('Valor', 0.01, icon=':material/money:')
tax = c.number_input('Taxa', 0.1, 100.0, 10.0, 0.1,icon=':material/percent:') / 100
calc = c.selectbox('Indicador', ['GGR', 'NGR']).lower()
result = format_currency(calculate_share_rate(value, tax, calc))
c.metric('Resultado', result, border=True)
