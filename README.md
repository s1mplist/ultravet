# Assistente de Ultrassom Veterinário (UltraVet)

Este projeto é um assistente virtual especializado em veterinária, com foco em exames de ultrassom. O assistente permite que veterinários tirem dúvidas, busquem informações para complementar diagnósticos e acessem referências a estudos e artigos científicos relevantes.

## 📋 Funcionalidades

- **Respostas a perguntas veterinárias**: Foco em exames de ultrassom e diagnóstico por imagem.
- **Referências Científicas**: Fornece referências a artigos e estudos relevantes para as respostas fornecidas.
- **Interface de Usuário Amigável**: Acessível via web ou aplicativo.
- **Integração com Bases de Dados**: Integração com APIs de bases de dados científicas (como PubMed).

## 🛠️ Tecnologias Utilizadas

- **LangChain**: Para o fluxo de conversação e gerenciamento de contexto.
- **OpenAI API (ChatGPT)**: Modelo de IA para responder perguntas e fornecer informações relevantes.
- **Backend**: Desenvolvido em Python usando FastAPI ou Flask.
- **Frontend**: Construído com React ou Vue.js para uma interface interativa.
- **Banco de Dados**: PostgreSQL ou MongoDB para armazenamento de dados.
- **Deploy**: Utilizando Docker para contêinerização e hospedagem em uma plataforma de nuvem (AWS, Azure, ou GCP).

## 🚀 Como Executar o Projeto

### Pré-requisitos

- Docker e Docker Compose instalados.
- Conta de nuvem configurada (AWS, Azure, ou GCP).
- Chave da API da OpenAI.

### Passos para Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/s1mplist/ultravet.git
   cd ultravet
   ```

2. Crie um arquivo `.env` na raiz do projeto e adicione suas credenciais:
   ```env
   OPENAI_API_KEY=sua-chave-api
   DATABASE_URL=sua-url-do-banco
   ```

3. Execute o Docker Compose para iniciar o backend e frontend:
   ```bash
   docker-compose up --build
   ```

4. Acesse o projeto no navegador:
   - Frontend: `http://localhost:3000`
   - Backend: `http://localhost:8000`

## 📚 Documentação da API

Para detalhes sobre as rotas da API e como utilizá-las, consulte o arquivo [API_DOCS.md](API_DOCS.md).

## 📈 Roadmap

- [x] Protótipo do backend e integração com ChatGPT.
- [x] Interface de usuário básica.
- [ ] Integração com bases de dados de referências científicas.
- [ ] Testes de usuários e refinamento.
- [ ] Deploy em produção.

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma _issue_ ou enviar um _pull request_ com melhorias e correções.

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📧 Contato

Para dúvidas ou sugestões, entre em contato:
- Email: gustavopinheiro.az@gmail.com
- LinkedIn: [Gustavo Cesar Pinheiro de Azevedo](https://www.linkedin.com/in/gustavo-pinheiro-azevedo/)

---

Feito com 💙 por [s1mplist](https://github.com/s1mplist).
