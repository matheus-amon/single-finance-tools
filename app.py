import streamlit as st

pages = {
    'Início': [
        st.Page('pages/home.py', title='Home', icon=':material/home:'),
    ],
    'Ferramentas': [
    	st.Page('pages/calculators.py', title='Calculadoras', icon=':material/calculate:')
    ]
}

pg = st.navigation(pages)
pg.run()
