{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "6ea48975",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "2242f872",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv(\"df_final_filtered.csv\", index_col=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dbd396b5",
   "metadata": {},
   "outputs": [],
   "source": [
    "col1,col2 = st.columns([2,1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "30a5a69b",
   "metadata": {},
   "outputs": [],
   "source": [
    "with col1:\n",
    "    countries = st.multiselect('Select one/ multiple countries', np.unique(df['country']))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "82e1c652",
   "metadata": {},
   "outputs": [],
   "source": [
    "year = col2.select_slider('Select a year', np.unique(df['year']))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "20006ff2",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_filtered = df.loc[(df.country.isin(countries))&(df.year==year),:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "c58a8767",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'df_filtered' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Input \u001b[0;32mIn [8]\u001b[0m, in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0m sns\u001b[38;5;241m.\u001b[39mlineplot(data \u001b[38;5;241m=\u001b[39m \u001b[43mdf_filtered\u001b[49m, x \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mGNI per capita\u001b[39m\u001b[38;5;124m'\u001b[39m, y \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mlife expectancy\u001b[39m\u001b[38;5;124m'\u001b[39m)\n",
      "\u001b[0;31mNameError\u001b[0m: name 'df_filtered' is not defined"
     ]
    }
   ],
   "source": [
    "sns.lineplot(data = df_filtered, x = 'GNI per capita', y = 'life expectancy')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "da99e698",
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
   "version": "3.8.12"
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": true,
   "sideBar": true,
   "skip_h1_title": false,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": false,
   "toc_position": {},
   "toc_section_display": true,
   "toc_window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
