# 🚀 Port Scanner com Tkinter

Este é um scanner de portas simples feito em Python com interface gráfica usando Tkinter. O programa permite realizar dois tipos de escaneamento:
- 🔍 **Quick Scan**: Verifica apenas as portas mais comuns.
- 🛠 **Full Scan**: Verifica todas as portas de 1 a 1024.

## 🎯 Funcionalidades
- 🌐 Resolve o IP a partir da URL digitada.
- 🔓 Escaneia portas abertas.
- 🔄 Usa delays aleatórios para evitar bloqueios por firewalls.
- 🖥 Exibe os resultados em uma interface gráfica.

## 📥 Instalação e Execução

1. Certifique-se de ter o Python instalado.
2. Instale as dependências necessárias (caso ainda não tenha o Tkinter):
   ```sh
   pip install tk
   ```
3. Execute o script:
   ```sh
   python nome_do_arquivo.py
   ```

## ⏳ Observação sobre o Timeout
O código usa um timeout aleatório para evitar bloqueios por firewalls e sistemas de detecção de varredura de portas. Se quiser remover essa limitação e escanear as portas mais rapidamente, altere ou remova a seguinte linha:

```python
socket.setdefaulttimeout(random.uniform(0.5, 1.5))
```

⚠️ Isso pode aumentar a chance de bloqueios ou detecção do escaneamento.

## ⚠️ Aviso Legal
Este software deve ser usado apenas para **fins educacionais** e testes em **redes próprias**. ❌ **Não utilize para escanear redes ou sistemas sem autorização**, pois isso pode ser **ilegal** dependendo da legislação local.

