from flask import Flask, request, render_template, redirect, url_for
from pytube import YouTube
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_video():
    link = request.form['link']
    path = request.form['path']
    
    try:
        yt = YouTube(link)
        ys = yt.streams.get_highest_resolution()
        ys.download(path)

        return f"""
        <h3>Download completo!</h3>
        <p>Título: {yt.title}</p>
        <p>Número de views: {yt.views}</p>
        <p>Tamanho do vídeo: {yt.length} segundos</p>
        <p>Avaliação do vídeo: {yt.rating}</p>
        """
    except Exception as e:
        return f"<h3>Ocorreu um erro: {str(e)}</h3>"

if __name__ == '__main__':
    app.run(debug=True)
