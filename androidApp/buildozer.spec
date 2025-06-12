# (Obrigatório) Título do seu aplicativo, como aparece no dispositivo Android
title = Device Data Collector

# (Obrigatório) Nome do pacote, usado para identificar seu app.
# Deve ser em minúsculas, sem espaços e com pontos (ex: com.suaempresa.seunomeapp)
package.name = devicedatacollector

# (Obrigatório) Domínio do pacote, geralmente o domínio da sua empresa ou seu nome.
# Altere 'com.suaempresa' para algo que faça sentido para você.
package.domain = com.projeto-x

# (Obrigatório) Versão do seu aplicativo. Use números.
version = 0.1

# (Obrigatório) O caminho para o seu arquivo Python principal.
# Se main.py estiver na raiz do projeto, use 'main.py'.
main.py = main.py

# (Obrigatório) Lista de requisitos Python que seu aplicativo Kivy utiliza.
# 'python3' e 'kivy' são essenciais para Kivy.
# 'requests' é necessário para a comunicação HTTP com seu backend Flask.
# 'python-for-android' é um requisito interno do Buildozer.
# As outras libs do seu requirements.txt (flask, pymysql, etc.) são para o backend
# e NÃO devem ser incluídas aqui.
requirements = python3,kivy,requests,python-for-android

# Versão da API Android que o APK será compilado para.
# Recomenda-se uma versão recente para compatibilidade e segurança.
# A API 33 (Android 13) é uma boa escolha atualmente.
android.api = 33

# (Opcional) A versão mínima da API Android suportada.
# Certifique-se de que é 21 ou superior.
android.minapi = 21

# Permissões Android que seu aplicativo precisa.
# 'INTERNET' é crucial para comunicação com o backend.
# 'READ_EXTERNAL_STORAGE' e 'WRITE_EXTERNAL_STORAGE' são solicitadas no seu main.py.
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# (Opcional) Caminho para o ícone do seu aplicativo.
# Se você tiver um arquivo 'icon.png' na raiz do seu projeto, pode descomentar e usar.
# icon.filename = %(source.dir)s/icon.png

# (Opcional) Adicione quaisquer outros arquivos ou diretórios que seu aplicativo Kivy precise.
# O Buildozer geralmente inclui todos os arquivos .py na source.dir, mas se você tiver
# outros tipos de arquivos ou subdiretórios específicos, liste-os aqui.
# Por exemplo, se 'collect_and_send_data.py' estiver em um subdiretório 'src':
# source.include_exts = py,png,jpg,kv
# source.include_dirs = src

# --- Outras configurações (geralmente não precisam de alteração inicial) ---
[buildozer]
# Nível de log (0 = silencioso, 1 = erro, 2 = aviso, 3 = informação, 4 = depuração)
log_level = 2
