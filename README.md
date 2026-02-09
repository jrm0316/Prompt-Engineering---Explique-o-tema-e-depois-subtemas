# Prompt Engineering - Explique o tema e depois subtemas

- Este repositório apresenta uma aplicação desenvolvida em Python que utiliza LangChain em conjunto com um modelo de linguagem da Groq (LLM) para gerar explicações educacionais de forma estruturada, previsível e reutilizável.
- O projeto vai além de uma simples chamada a um modelo de IA. Ele demonstra como controlar o comportamento da IA por meio de engenharia de prompts, aplicando boas práticas usadas em aplicações reais de backend com LLMs.


Propósito do projeto
O objetivo deste projeto é demonstrar como arquitetar uma solução com IA em que:
- o formato da resposta é controlado pelo desenvolvedor
- o texto do prompt é separado da lógica do código
- a IA se comporta como um componente previsível do sistema

Em vez de “perguntar qualquer coisa para a IA”, o sistema atua como um assistente educacional, capaz de explicar qualquer tema seguindo uma estrutura fixa, semelhante a documentação técnica ou material didático.

Esse tipo de abordagem é amplamente utilizado em:
- chatbots corporativos
- copilotos de desenvolvimento
- APIs inteligentes
- ferramentas internas com IA


Como a IA responde
Para cada tema informado, a IA gera a resposta seguindo exatamente a estrutura definida no prompt:
- Definição simples
- Para que serve
- Exemplo prático
- Quando usar

Esse controle garante que a saída possa ser:
- exibida em interfaces
- salva em arquivos
- reutilizada em outros sistemas
- integrada a APIs e fluxos de negócio


Tecnologias e conceitos utilizados
- Python
- LangChain
- Groq (LLM)
- PromptTemplate
- LCEL (LangChain Expression Language)
- Engenharia de Prompts
- Integração de IA no backend


Estrutura do projeto
assistente-educacional-langchain/
│
├── main.py
├── .env
└── README.md


Como executar o projeto

  1.) Clonar o repositório
    git clone https://github.com/seu-usuario/Prompt-Engineering---Explique-o-tema-e-depois-subtemas.git
    cd assistente-educacional-langchain

  2.) Instalar as dependências
    pip install langchain langchain-groq python-dotenv

  3.) Configurar a variável de ambiente
Crie um arquivo .env na raiz do projeto e adicione sua chave da Groq:

    GROQ_API_KEY=SUA_CHAVE_AQUI

  4.) Executar o script
    python main.py


Alterando o tema analisado
- O tema explicado pela IA é totalmente dinâmico.
- Basta alterar o valor enviado para a chain:

resposta = chain.invoke({
    "tema": "Python"
})


Exemplos de temas possíveis:
- APIs REST
- Programação Orientada a Objetos
- SQL
- Docker
- Inteligência Artificial
- Estruturas de Dados


Por que este projeto é relevante?
Este projeto demonstra habilidades importantes para aplicações modernas com IA, como:
- controle do formato de saída de LLMs
- uso correto de PromptTemplate
- separação entre lógica e texto
- arquitetura de prompts reutilizáveis
- integração prática de IA em sistemas backend
Esses conceitos são frequentemente exigidos em projetos profissionais com IA aplicada.


Resumo profissional
- Aplicação em Python utilizando LangChain e LLM (Groq) para geração de respostas educacionais estruturadas, com foco em engenharia de prompts, controle de formato e integração de IA no backend.


Possíveis evoluções do projeto
- Entrada interativa via terminal (CLI)
- Salvamento automático das respostas em arquivos
- Retorno estruturado em JSON
- Exposição do serviço via API (FastAPI)
- Interface web simples
