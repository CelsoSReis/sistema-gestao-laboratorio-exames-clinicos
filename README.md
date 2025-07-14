# 🧪 Sistema de Gestão para Laboratório de Exames Clínicos

## Descrição
Uma **aplicação completa para gerenciamento de laboratórios clínicos**, ideal para centralizar e automatizar a **gestão de pacientes, exames e resultados**. Projetado para garantir **eficiência**, **controle de dados** e **segurança** em todas as etapas: do agendamento até a entrega dos resultados.

## 🔍 Principais Funcionalidades
- Cadastro e gerenciamento de **pacientes**, **médicos**, **convênios** e **exames**
- **Agendamento de exames** com verificação de preparo
- Geração de **protocolos de atendimento**
- **Listagem de exames pendentes**
- Impressão de **etiquetas** para identificação de amostras
- Controle de **acesso por tipo de usuário**
- Emissão de **relatórios clínicos em PDF**

## ⚙️ Tecnologias Utilizadas

| Camada        | Tecnologias                   |
|---------------|-------------------------------|
| Linguagem     | 🐍 Python                     |
| Framework Web | 🌐 Django                     |
| Frontend      | 🎨 Bootstrap                  |
| Banco de Dados| 🐘 PostgreSQL                 |
| Outros        | 🗂️ Django Admin, PDFKit (para geração de relatórios) |

## 🏗️ Arquitetura & Boas práticas
- Organização modular por apps no Django
- Utilização de **views genéricas** e **class-based views**
- Templates com **Bootstrap responsivo**
- Sistema de **autenticação e permissões**
- Separação entre ambientes de desenvolvimento e produção

## 🚀 Como executar o projeto

### Pré-requisitos
- Python 3.10+
- PostgreSQL
- Pip ou Pipenv
- Virtualenv

### Passos para instalação

```bash
# Clone o repositório
git clone https://github.com/CelsoSReis/sistema-gestao-laboratorio-exames-clinicos.git
cd sistema-gestao-laboratorio-exames-clinicos

# Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Configure o banco de dados no settings.py

# Execute as migrações
python manage.py migrate

# Crie um superusuário
python manage.py createsuperuser

# Inicie o servidor
python manage.py runserver
