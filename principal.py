import streamlit as st

st.title('Questionario feminino pos Fertilizacao In Vitro (FIV)')

dimensao1 = st.container()
dimensao1.write('Dimensao 1 Competencia tecnica medica')
dimensao1.selectbox('Medical care',("I received the best possible medical care (examinations and treatments) as far as I can tell",
                                    "I DO NOT received the best possible medical care (examinations and treatments) as far as I can tell"))
dimensao1.selectbox('Pain relief and physical care',("I received effective pain relief during oocyte aspiration.",
                                                     "I received the best possible physical care during oocyte aspiration (as far as I can tell)."))
dimensao1.selectbox('Waiting time',("I received my first appointment at the clinic within acceptable waiting time.",
                                    "I received this treatment within acceptable waiting time."))
dimensao2 = st.container()
dimensao2.write('Dimensao 2 Condicoes tecnico-fisicas ')
dimensao2.selectbox('Care room characteristics',("I had access to a pleasant room while waiting for oocyte aspiration.",
                                                 "I had access to a comfortable bed before and after oocyte aspiration.",
                                                 "I had access to a pleasant treatment room during oocyte aspiration and embryo transfer."))
dimensao3 = st.container()
dimensao3.write('Dimensao 3 Abordagem de orientacao')
dimensao3.selectbox('Information during treatment',("I received the best possible medical care (examinations and treatments) as far as I can tell",
                                                   "I received good informationregarding the drugs I needed, so that I understood their effects, and how they should be administered.",
                                                    "I received good information about results from examinations (for example ultrasound, hormone and sperm analyses)."))
dimensao3.selectbox('Information after treatment',("I received good informationregarding the fertilization and embryo development at the time of embryo transfer.",
                                                   "I received good informationregarding the time between embryo transfer and pregnancy test."))
dimensao3.selectbox('Participation',("I had good opportunitiesto participate in the decisions that applied to my treatment",
                                     "My carewasdetermined bymyownrequestsneedsratherthanthe staff’s procedures."))
dimensao3.selectbox('Responsibility/continuity',("I received good information about which doctor was responsible for my treatment.",
                                                 "I received good information about whichmidwife was responsible for my treatment.",
                                                 "I met the same doctor at examinations and treatment during this treatment period.",
                                                 "I met the same midwife at examinations and interviews during this treatment period."))
dimensao3.selectbox('The Staff’s respect/commitment/empathy',("The doctors were respectful towards me.",
                                                              "The doctors showed commitment; ‘cared about me’.",
                                                              "The doctors seemed to understand how I experienced my situation.",
                                                              "The midwives/nurses/laboratory personnel were respectful towards me.",
                                                              "The midwives/nurses/laboratory personnel showed commitment; ‘cared about me’.",
                                                              "Themidwives/nurses/laboratory personnel seemedto understand how I experienced my situation."))
dimensao4 = st.container()
dimensao4.write('Dimensao 4 Atmosfera socio-cultural')
dimensao4.selectbox('Atmosphere and environment',("I received the best possible medical care (examinations and treatments) as far as I can tell"))
