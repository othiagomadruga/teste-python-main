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

# O diretório de onde os arquivos fonte do app serão copiados.
# O ponto '.' significa o diretório atual onde o Buildozer está sendo executado.
source.dir = .

# (Obrigatório) Todas as dependências Python que seu aplicativo Kivy utiliza.
# AQUI ESTÁ A LINHA CORRIGIDA: Fixando python-for-android para a versão 2021.08.02 para maior estabilidade.
requirements = python3==3.8.10,kivy,requests,python-for-android==2021.08.02

# Versão da API Android que o APK será compilado para.
android.api = 29

# A versão mínima da API Android suportada.
android.minapi = 29

# Permissões Android que seu aplicativo precisa.
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# android.p4a_channel foi removido, pois a versão fixa tem precedência.

# Habilita o suporte a Multidex, necessário para aplicativos grandes
# ou com muitas bibliotecas, para evitar limites de métodos no Android.
android.enable_multidex = True

# Aceita automaticamente as licenças do Android SDK.
android.accept_sdk_license = True

# Especifica ambas as arquiteturas de CPU Android para as quais o APK será construído.
android.archs = armeabi-v7a, arm64-v8a

# Especifica a versão do NDK para 25b, conforme recomendado.
android.ndk = 25b

# exclude_recipes = libffi foi removido/comentado.

# (Opcional) URL da sua icon (ex: icon.png na raiz do projeto)
# icon.filename = %(source.dir)s/icon.png

# (Opcional) Excluir arquivos/diretórios desnecessários
# exclude_dir = tests, docs


[buildozer]
# Nível de log (0 = silencioso, 1 = erro, 2 = aviso, 3 = informação, 4 = depuração)
log_level = 4
