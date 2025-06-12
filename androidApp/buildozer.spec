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
# AQUI ESTÁ A LINHA CORRIGIDA: Especificando explicitamente a versão do Python 3.
requirements = python3==3.9,kivy,requests,python-for-android==2022.09.04

# Versão da API Android que o APK será compilado para.
android.api = 29

# A versão mínima da API Android suportada.
android.minapi = 29

# Permissões Android que seu aplicativo precisa.
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# Removido android.p4a_channel = master, pois a versão fixa tem precedência.
# android.p4a_channel = master

# Habilita o suporte a Multidex, necessário para aplicativos grandes
# ou com muitas bibliotecas, para evitar limites de métodos no Android.
android.enable_multidex = True

# Aceita automaticamente as licenças do Android SDK.
android.accept_sdk_license = True

# Especifica ambas as arquiteturas de CPU Android para as quais o APK será construído.
android.archs = armeabi-v7a, arm64-v8a

# AQUI ESTÁ A LINHA CORRIGIDA: Especificando a versão do NDK para 23b.
android.ndk = 23b

# AQUI ESTÁ A LINHA CORRIGIDA: Exclui a receita de compilação da libffi.
exclude_recipes = libffi

# (Opcional) URL da sua icon (ex: icon.png na raiz do projeto)
# icon.filename = %(source.dir)s/icon.png

# (Opcional) Excluir arquivos/diretórios desnecessários
# exclude_dir = tests, docs


[buildozer]
# Nível de log (0 = silencioso, 1 = erro, 2 = aviso, 3 = informação, 4 = depuração)
log_level = 4
