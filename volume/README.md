# Controle de Volume para Windows

Este projeto é um aplicativo simples que permite controlar o volume do Windows usando teclas de atalho, funcionando discretamente com um ícone na bandeja do sistema.

## Funcionalidades

- Use **+** para aumentar o volume
- Use **-** para diminuir o volume
- Clique no ícone na bandeja do sistema para acessar o menu
- Pressione **Shift + ESC** para encerrar o programa

## Requisitos

- Windows 10 ou Windows 11
- Python 3.8 ou superior
- Bibliotecas: keyboard, pystray, Pillow

## Instalação e Configuração

### 1. Configurar ambiente virtual

Abra o PowerShell como administrador e execute:

```powershell
# Permitir execução de scripts
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

# Navegar até a pasta do projeto
cd C:\caminho\para\o\projeto

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
.\venv\Scripts\Activate
```

### 2. Instalar dependências

Com o ambiente virtual ativado, instale as bibliotecas necessárias:

```powershell
pip install keyboard pystray Pillow pyinstaller
```

Ou use o arquivo requirements.txt:

```powershell
pip install -r requirements.txt
```

### 3. Gerar executável

#### Criar arquivo .spec personalizado

Crie ou modifique o arquivo `cv.spec` incluindo as dependências ocultas:

```python
# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['cv.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['pystray', 'PIL', 'PIL._tkinter_finder'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='cv',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
```

#### Compilar o executável

```powershell
# Encerre qualquer instância existente do programa
taskkill /f /im cv.exe

# Gere o executável
python -m PyInstaller cv.spec
```

O executável será gerado na pasta `dist`.

### 4. Configurar inicialização automática com privilégios de administrador

Para que o programa seja iniciado automaticamente com o Windows **como administrador**:

#### Método 1: Usando Agendador de Tarefas (Recomendado)

1. Pressione `Win + R`, digite `taskschd.msc` e pressione Enter
2. No painel direito, clique em **"Criar Tarefa..."** (não "Criar Tarefa Básica")
3. Na aba **Geral**:
   - Nome: `Controle de Volume`
   - Marque a opção **"Executar com privilégios mais altos"**
   - Configure para: `Windows 10` ou `Windows 11`
4. Na aba **Disparadores**:
   - Clique em **Novo...**
   - Iniciar a tarefa: `Ao fazer logon`
   - Marque **"Habilitado"**
   - Clique em **OK**
5. Na aba **Ações**:
   - Clique em **Novo...**
   - Ação: `Iniciar um programa`
   - Programa/script: Clique em **Procurar** e selecione `C:\git\python\volume\dist\cv.exe`
   - Clique em **OK**
6. Na aba **Condições**:
   - Desmarque **"Iniciar a tarefa apenas se o computador estiver conectado à energia CA"** (para notebooks)
7. Na aba **Configurações**:
   - Marque **"Permitir que a tarefa seja executada sob demanda"**
   - Marque **"Se a tarefa falhar, reiniciar a cada: 1 minuto"**
8. Clique em **OK** para salvar

#### Método 2: Usando atalho na pasta de inicialização

1. Navegue até a pasta `dist` onde está o `cv.exe`
2. Clique com botão direito no `cv.exe` → **Criar atalho**
3. Clique com botão direito no atalho → **Propriedades**
4. Clique no botão **Avançado...**
5. Marque a opção **"Executar como administrador"**
6. Clique em **OK** e depois em **OK** novamente
7. Pressione `Win + R`, digite `shell:startup` e pressione Enter
8. Mova o atalho criado para esta pasta de inicialização

**Nota:** O Método 2 pode exibir uma solicitação UAC a cada inicialização. O Método 1 (Agendador de Tarefas) é mais silencioso e recomendado.

## Solução de problemas

### Erro de módulo não encontrado

Se você receber o erro `ModuleNotFoundError: No module named 'pystray'` ao executar o programa, verifique:

1. Se as bibliotecas estão instaladas corretamente no ambiente virtual ativo
2. Se você gerou o executável usando o arquivo .spec modificado com os `hiddenimports`

### Erro de permissão ao compilar

Se ocorrerem erros de permissão ao compilar o executável:

1. Encerre todas as instâncias do programa com `taskkill /f /im cv.exe`
2. Tente compilar novamente
3. Se persistir, reinicie o computador e tente novamente

### Antivírus bloqueando o executável

Se o Windows Defender ou outro antivírus bloquear o `cv.exe` com erro "Acesso negado" ou deletar o arquivo:

#### Adicionar exceção no Windows Defender:

1. Pressione `Win + I` para abrir Configurações
2. Vá em **Privacidade e segurança** → **Segurança do Windows**
3. Clique em **Proteção contra vírus e ameaças**
4. Clique em **Gerenciar configurações**
5. Role até **Exclusões** e clique em **Adicionar ou remover exclusões**
6. Clique em **+ Adicionar uma exclusão** → **Pasta**
7. Navegue e selecione `C:\git\python\volume\dist`

#### Via PowerShell (como Administrador):

```powershell
Add-MpPreference -ExclusionPath "C:\git\python\volume\dist"
```

**Nota:** O executável inclui informações de versão e metadados para reduzir falsos positivos, mas alguns antivírus podem ainda assim bloqueá-lo por ser gerado com PyInstaller.

## Desenvolvimento

O código fonte está organizado da seguinte forma:

- Importações e constantes no início
- Funções para controle de volume
- Configurações de atalhos de teclado
- Funções para o ícone na bandeja do sistema
- Inicialização do ícone em thread separada
- Loop principal aguardando o comando de saída
