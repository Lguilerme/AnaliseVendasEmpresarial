# 📊 Análise Empresarial de Vendas com Python

Projeto de análise exploratória de dados de vendas de uma empresa fictícia, desenvolvido em Python com foco em limpeza, transformação e visualização de dados para geração de insights estratégicos.

---

## 🎯 Objetivo

Explorar um dataset de vendas para responder perguntas de negócio como:

- Qual categoria de produto gera mais receita?
- Quais dias da semana concentram mais vendas?
- Qual o perfil dos clientes VIP vs. não VIP?
- Como as vendas se distribuem ao longo dos meses?

---

## 🛠️ Tecnologias Utilizadas

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=python&logoColor=white)

---

## 📁 Estrutura do Projeto

```
AnaliseVendasEmpresarial/
├── exercício_python.py          # Script principal de análise
├── requirements.txt             # Dependências do projeto
├── README.md                    # Documentação do projeto
└── dados_vendas_empresa_1.xlsx  # Dataset utilizado
```

---

## 🔍 O que foi analisado

- **Limpeza e padronização** dos dados — tratamento de colunas, tipos e valores nulos
- **Estatísticas descritivas** — média, soma, contagem, máximo e mínimo por categoria
- **Segmentação de clientes** — criação da coluna `Status` (VIP / Não VIP) com base no valor de venda
- **Análise temporal** — extração de ano, mês, dia e dia da semana a partir da data de venda
- **Visualizações** — gráficos de barras, histogramas, pizza, dispersão, área e boxplots

---

## 📈 Principais Visualizações

| Gráfico | Descrição |
|---|---|
| Barras por categoria | Quantidade e total de vendas por categoria |
| Histograma | Distribuição dos valores de venda |
| Pizza | Participação percentual de cada categoria |
| Boxplot | Distribuição de vendas por dia da semana, mês e categoria |
| Dispersão | Relação entre dia da semana e total de venda |
| Barras agrupadas | Comparação VIP vs. Não VIP por categoria |

---

## 🚀 Como Executar

**1. Clone o repositório**
```bash
git clone https://github.com/Lguilerme/AnaliseVendasEmpresarial.git
cd AnaliseEmpresarial
```

**2. Crie e ative um ambiente virtual**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

**3. Instale as dependências**
```bash
pip install -r requirements.txt
```

**5. Execute o script**
```bash
python "exercício_python.py"
```

---

## 📬 Contato

Feito por **Luis Guilherme** — [LinkedIn](https://www.linkedin.com/in/luis-gui/) • [GitHub](https://github.com/Lguilerme)
