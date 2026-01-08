import streamlit as st

st.markdown('### Calculadora de Share Rate')

def calculate_share_rate(value, tax, calc):
	ngr = (value - (value*0.12)) * tax
	ggr = value * tax

	if calc == 'ggr':
		return ggr
	else:
		return ngr


value = st.number_input('Valor', 0.01, icon=':material/money:')
tax = st.number_input('Taxa', 0.01, 100.00, icon=':material/percent:') / 100
calc = st.selectbox('Indicador', ['GGR', 'NGR']).lower()

st.metric('Resultado', calculate_share_rate(value, tax, calc))
