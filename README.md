# Automação LinkedIn 🚀

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green)
![Build](https://img.shields.io/badge/Build-PyInstaller-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## Descrição

Este projeto é um **bot de automação para LinkedIn** desenvolvido em **Python** usando **Selenium** e **CustomTkinter**.  

Ele permite:

- Enviar **mensagens automáticas** para conexões já aceitas.  
- Enviar **convites de conexão** filtrando por cargo ou perfil.  
- Acompanhar o **progresso em tempo real** através de barra de progresso e mensagens na interface.  

> ⚠️ **Atenção:** Este projeto é apenas para fins educacionais e de portfólio. Automatizar interações massivas no LinkedIn pode violar os Termos de Serviço.

## Funcionalidades

- Interface gráfica amigável (Tkinter + CustomTkinter)  
- Barra de progresso para acompanhar envios  
- Mensagens personalizadas com o nome do contato  
- Filtragem de conexões de 2º grau  
- Fechamento automático de janelas de conversa  

## Tecnologias Utilizadas

- Python 3.10+  
- Selenium WebDriver  
- CustomTkinter  
- CTkMessagebox  
- PyInstaller (para gerar `.exe`)  

## Instalação

### 1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/linkedin-automation.git
cd linkedin-automation
```

### 2. Instale as dependências:
```bash
pip install -r requirements.txt
```
### 3. Uso
#### Execute o script principal:
```bash
python linkedin-automation-python.py
```
- Escolha entre Enviar Mensagens ou Enviar Conexões
- Preencha os campos (quantidade, cargo, mensagem)
- Clique em Iniciar e acompanhe a barra de progresso

#### Criando um Executável (.exe)

Para distribuir o programa sem precisar do Python instalado:
Instale o PyInstaller:
```bash
pip install pyinstaller
```
Gere o .exe:
```bash
pyinstaller --onefile --windowed linkedin-automation-python.py
```
- O executável será criado na pasta dist/
- Use --windowed para abrir sem terminal.

### Observações
- O script utiliza perfil do Chrome (user-data-dir) para manter login.
- Use com responsabilidade, de preferência em contas de teste ou pessoais.
- Nunca compartilhe suas senhas no código.

### Licença

Este projeto está licenciado sob a MIT License.
