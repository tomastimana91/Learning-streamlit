# -*- coding: utf-8 -*-
"""
Created on Tue May 20 14:32:39 2025

@author: Pedregal
"""

import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
st.title("Área del triangulo")
base=st.text_input("Ingresa base del triangulo")
altura=st.text_input("Ingresa la altura del triangulo")
if base!="" and altura !="":
    base=float(base)
    altura=float(altura)
if st.button("Calcular área"):
    area=base*altura/2
    st.write("El area del triangulo es:",area)
    A = (0, 0)
    B = (base, 0)
    C = (base / 2, altura)
    fig, ax = plt.subplots(figsize=(4,4))
    x = [A[0], B[0], C[0], A[0]]
    y = [A[1], B[1], C[1], A[1]]
    ax.plot(x, y, 'b-')
    ax.fill(x, y, 'skyblue', alpha=0.3)
    # Añadir etiquetas y límites
    ax.set_title("Triángulo")
    ax.set_xlim(-1, base + 1)
    ax.set_ylim(-1, altura + 1)
    ax.set_aspect('equal')
    col1, col2 = st.columns([1, 1.5])
    with col1:
        st.pyplot(fig)