import streamlit as st

# CSS correctamente embebido
st.markdown("""
<style>
body {
    background-color: #0f172a;
    color: white;
}

.container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
}

.card {
    background: #1e293b;
    padding: 40px 20px;
    border-radius: 16px;
    margin-bottom: 20px;
}

a {
    color: #38bdf8;
    text-decoration: none;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# Contenido HTML del portafolio
html = """
<h1>🚀 Mi Portafolio</h1>

<div class="container">

<div class="card">
<h3>Ctrl Voice</h3>
<a href="https://github.com/Palacios21/Ctrl_voice" target="_blank">Ver proyecto</a>
</div>

<div class="card">
<h3>Receptor MQTT</h3>
<a href="https://github.com/Palacios21/Receptor_Mqtt" target="_blank">Ver proyecto</a>
</div>

<div class="card">
<h3>Análisis de Texto</h3>
<a href="https://github.com/Palacios21/analisis_de_texto" target="_blank">Ver proyecto</a>
</div>

<div class="card">
<h3>Imagen a Audio</h3>
<a href="https://github.com/Palacios21/img-audio" target="_blank">Ver proyecto</a>
</div>

<div class="card">
<h3>Sentimientos</h3>
<a href="https://github.com/Palacios21/Sentimientos--_-" target="_blank">Ver proyecto</a>
</div>

<div class="card">
<h3>Lectura de Imágenes</h3>
<a href="https://github.com/Palacios21/Lect_img" target="_blank">Ver proyecto</a>
</div>

</div>
"""

# Renderizar HTML
st.markdown(html, unsafe_allow_html=True)
