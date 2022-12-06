import streamlit as st

st.title('Questionario feminino pos Fertilizacao In Vitro (FIV)')

dimensao1 = st.container()
dimensao1.write('Dimensao 1 Competencia tecnica medica')
dimensao1.selectbox('Medical care',("I received the best possible medical care (examinations and treatments) as far as I can tell","I DO NOT received the best possible medical care (examinations and treatments) as far as I can tell"))
dimensao2 = st.container()
dimensao2.write('Dimensao 2 Condicoes tecnico-fisicas ')
dimensao2.selectbox('Care room characteristics',("I had access to a pleasant room while waiting for oocyte aspiration.",
                                                 "I had access to a comfortable bed before and after oocyte aspiration.",
                                                 "I had access to a pleasant treatment room during oocyte aspiration and embryo transfer."))
dimensao3 = st.container()
dimensao3.write('Dimensao 3 Abordagem de orientacao')
dimensao3.selectbox('Information during treatment',"I received the best possible medical care (examinations and treatments) as far as I can tell")
dimensao4 = st.container()
dimensao4.write('Dimensao 4 Atmosfera socio-cultural')
dimensao4.selectbox('Atmosphere and environment',"I received the best possible medical care (examinations and treatments) as far as I can tell")
