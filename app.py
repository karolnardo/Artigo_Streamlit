{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "c2ff78f7",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "import streamlit as st"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "374f0577",
   "metadata": {},
   "outputs": [],
   "source": [
    "# importando os dados\n",
    "dados = pd.read_csv('estoque.csv')\n",
    "\n",
    "st.title('Análise de estoque\\n')\n",
    "st.write('Nesse projeto vamos analisar a quantidade de produtos em estoque, por categoria, de uma base de dados de produtos de supermercado')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "7dacd412",
   "metadata": {},
   "outputs": [],
   "source": [
    "# filtros para a tabela\n",
    "checkbox_mostrar_tabela = st.sidebar.checkbox('Mostrar tabela')\n",
    "if checkbox_mostrar_tabela:\n",
    "\n",
    "    st.sidebar.markdown('## Filtro para a tabela')\n",
    "\n",
    "    categorias = list(dados['Categoria'].unique())\n",
    "    categorias.append('Todas')\n",
    "\n",
    "    categoria = st.sidebar.selectbox('Selecione a categoria para apresentar na tabela', options = categorias)\n",
    "\n",
    "    if categoria != 'Todas':\n",
    "        df_categoria = dados.query('Categoria == @categoria')\n",
    "        mostra_qntd_linhas(df_categoria)      \n",
    "    else:\n",
    "        mostra_qntd_linhas(dados)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "0616d483",
   "metadata": {},
   "outputs": [],
   "source": [
    "# função para selecionar a quantidade de linhas do dataframe\n",
    "def mostra_qntd_linhas(dataframe):\n",
    "\n",
    "    qntd_linhas = st.sidebar.slider('Selecione a quantidade de linhas que deseja mostrar na tabela', min_value = 1, max_value = len(dataframe), step = 1)\n",
    "\n",
    "    st.write(dataframe.head(qntd_linhas).style.format(subset = ['Valor'], formatter=\"{:.2f}\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "a6056b4c",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'plot' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_13756/1434224104.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[0mcategoria_grafico\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mst\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msidebar\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mselectbox\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'Selecione a categoria para apresentar no gráfico'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0moptions\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mdados\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'Categoria'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0munique\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 5\u001b[1;33m \u001b[0mfigura\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mplot\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdados\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcategoria_grafico\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      6\u001b[0m \u001b[0mst\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpyplot\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfigura\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'plot' is not defined"
     ]
    }
   ],
   "source": [
    "# filtro para o gráfico\n",
    "st.sidebar.markdown('## Filtro para o gráfico')\n",
    "\n",
    "categoria_grafico = st.sidebar.selectbox('Selecione a categoria para apresentar no gráfico', options = dados['Categoria'].unique())\n",
    "figura = plot_estoque(dados, categoria_grafico)\n",
    "st.pyplot(figura)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8dd91770",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "de427b11",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
