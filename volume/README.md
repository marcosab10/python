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

### 4. Configurar inicialização automática

Para que o programa seja iniciado automaticamente com o Windows:

1. Pressione `Win + R` e digite `shell:startup` para abrir a pasta de inicialização
2. Copie o arquivo `cv.exe` (ou crie um atalho) da pasta `dist` para a pasta de inicialização

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

## Desenvolvimento

O código fonte está organizado da seguinte forma:

- Importações e constantes no início
- Funções para controle de volume
- Configurações de atalhos de teclado
- Funções para o ícone na bandeja do sistema
- Inicialização do ícone em thread separada
- Loop principal aguardando o comando de saída
