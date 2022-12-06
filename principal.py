import streamlit as st

st.title('Questionario feminino pos Fertilizacao In Vitro (FIV)')

dimensao1 = st.container()
dimensao1.write('Dimensão 1 Competência médico-técnica')
dimensao1.radio('Cuidados médicos',("Recebi os melhores cuidados médicos possíveis (exames e tratamentos), tanto quanto posso dizer",
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
dimensao3.selectbox('Informações durante o tratamento',("Recebi os melhores cuidados médicos possíveis (exames e tratamentos), tanto quanto posso dizer",
                                                   "Recebi boas informações sobre os medicamentos de que precisava, para entender seus efeitos e como devem ser administrados.",
                                                    "Recebi boas informações sobre os resultados dos exames (por exemplo, ultrassom, análises hormonais e de esperma)."))
dimensao3.selectbox('Informações após o tratamento',("Recebi boas informações sobre a fertilização e o desenvolvimento do embrião no momento da transferência do embrião.",
                                                   "Recebi boas informações sobre o tempo entre a transferência do embrião e o teste de gravidez."))
dimensao3.radio('Participação',("Tive boas oportunidades de participar das decisões que se aplicavam ao meu tratamento.",
                                     "Meu atendimento foi determinado por minhas próprias necessidades de solicitações, e não pelos procedimentos da equipe."))
dimensao3.selectbox('Responsabilidade/continuidade',("Recebi boas informações sobre qual médico era o responsável pelo meu tratamento.",
                                                 "Recebi boas informações sobre qual parteira era responsável pelo meu tratamento.",
                                                 "Encontrei o mesmo médico em exames e tratamento durante esse período de tratamento.",
                                                 "Conheci a mesma parteira em exames e entrevistas durante esse período de tratamento."))
dimensao3.selectbox('Respeito/comprometimento/empatia da Equipe',("Os médicos foram respeitosos comigo.",
                                                              "Os médicos demonstraram comprometimento; ‘se importavam comigo’.",
                                                              "Os médicos pareciam entender como estava minha situação.",
                                                              "As parteiras/enfermeiras/pessoal do laboratório foram respeitosas comigo.",
                                                              "As parteiras/enfermeiras/pessoal do laboratório demonstraram comprometimento; ‘se importavam comigo’.",
                                                              "As parteiras/enfermeiras/pessoal do laboratório pareciam entender como eu vivenciava minha situação."))
dimensao4 = st.container()
dimensao4.write('Dimensão 4 Atmosfera sócio-cultural')
dimensao4.selectbox('Atmosfera e ambiente',("Havia um ambiente agradável na clínica",
                                            "Meu parceiro foi bem tratado.",
                                            "Fiz exames e entrevistas em privado sem perturbações."))

if st.button('Enviar respostas'):
  st.write('Obrigado por responder.')
