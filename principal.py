import streamlit as st

st.title('Questionario feminino pos Fertilizacao In Vitro (FIV)')

dimensao1 = st.container()
dimensao1.write('Dimensão 1 Competência médico-técnica')
dimensao1.selectbox('Cuidados médicos',("Recebi os melhores cuidados médicos possíveis (exames e tratamentos), tanto quanto posso dizer",
                                    "NÃO recebi os melhores cuidados médicos possíveis (exames e tratamentos), tanto quanto posso dizer"))
dimensao1.selectbox('Alívio da dor e cuidados físicos',("Recebi alívio eficaz da dor durante a aspiração de ovócitos.",
                                                     "Recebi o melhor cuidado físico possível durante a aspiração do oócito (tanto quanto posso dizer)."))
dimensao1.selectbox('Tempo de espera',("Recebi minha primeira consulta na clínica dentro do tempo de espera aceitável.",
                                    "Recebi este tratamento dentro do tempo de espera aceitável."))
dimensao2 = st.container()
dimensao2.write('Dimensão 2 Condições físico-técnicas')
dimensao2.selectbox('Características da sala de atendimento',("Tive acesso a uma sala agradável enquanto esperava pela aspiração de ovócitos.",
                                                 "Tive acesso a uma cama confortável antes e depois da aspiração de ovócitos.",
                                                 "Tive acesso a uma agradável sala de tratamento durante a aspiração de oócitos e transferência de embriões."))
dimensao3 = st.container()
dimensao3.write('Dimensão 3 Abordagem orientada para o auto-reconhecimento')
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
dimensao4.write('Dimensão 4 Atmosfera sócio-cultural')
dimensao4.selectbox('Atmosphere and environment',("I received the best possible medical care (examinations and treatments) as far as I can tell"))
