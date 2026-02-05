# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

prompt = PromptTemplate(
    input_variables=["tema"],
    template="""
    Explique o tema abaixo seguindo exatamente esta estrutura: # Tudo isso, é prompt engineering

    - Definição simples   # Aqui também
    - Para que serve      # Aqui também
    - Exemplo prático     # Aqui também
    - Quando usar         # Aqui também

    Tema: {tema} # Continua sendo dinâmico
"""
)

chain = prompt | llm

resposta = chain.invoke({
    "tema": "Python" # Troco esta linha por qualquer outra, e ele pesquisa sobre.
})

print(resposta.content)
