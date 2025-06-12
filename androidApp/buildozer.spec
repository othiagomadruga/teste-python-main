[app]
# (Obrigatório) Título do seu aplicativo, como aparece no dispositivo Android
title = Device Data Collector

# (Obrigatório) Nome do pacote, usado para identificar seu app.
# Deve ser em minúsculas, sem espaços e com pontos (ex: com.suaempresa.seunomeapp)
package.name = devicedatacollector

# (Obrigatório) Domínio do pacote, geralmente o domínio da sua empresa ou seu nome.
# Altere 'com.suaempresa' para algo que faça sentido para você.
package.domain = com.suaempresa

# (Obrigatório) Versão do seu aplicativo. Use números.
version = 0.1

# (Obrigatório) O caminho para o seu arquivo Python principal.
main.py = main.py

# AQUI ESTÁ A NOVA LINHA: O diretório de onde os arquivos fonte do app serão copiados.
# O ponto '.' significa o diretório atual onde o Buildozer está sendo executado.
source.dir = .

# (Obrigatório) Todas as dependências Python que seu aplicativo Kivy utiliza.
requirements = python3,kivy,requests,python-for-android

# Versão da API Android que o APK será compilado para.
android.api = 33

# (Opcional) A versão mínima da API Android suportada.
android.minapi = 21

# Permissões Android que seu aplicativo precisa.
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# (Opcional) URL da sua icon (ex: icon.png na raiz do projeto)
# icon.filename = %(source.dir)s/icon.png

# (Opcional) Excluir arquivos/diretórios desnecessários
# exclude_dir = tests, docs


[buildozer]
# Nível de log (0 = silencioso, 1 = erro, 2 = aviso, 3 = informação, 4 = depuração)
log_level = 4
