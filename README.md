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

## 🖥 Interface
   <div style="background-color:#2c2c2c; padding:10px; border-radius:10px; text-align:center; display: flex; justify-content: center;">

<table style="width:80%; margin:auto; text-align:center;">
  <tr>
    <td style="text-align:center;">
      <img src="https://github.com/Andrey-Soares8/Portscanner/blob/main/src/Interface%20principal.png" alt="Interface principal do app" style="width:90%; border: 1px solid transparent;"/>
      <p style="color:white;">Interface Gráfica</p>
    </td>
    <td style="text-align:center;">
      <img src="https://github.com/Andrey-Soares8/Portscanner/blob/main/src/Url%20ou%20ip%20(2).png" alt="Entrada para URL ou IP" style="width:90%; border: 1px solid transparent;"/>
      <p style="color:white;">Digite sua URL ou IP</p>
    </td>
  </tr>
  <tr>
    <td style="text-align:center;">
      <img src="https://github.com/Andrey-Soares8/Portscanner/blob/main/src/scan%20rapido%20ou%20full%20(3).png" alt="Opção de Quick Scan ou Full Scan" style="width:90%; border: 1px solid transparent;"/>
      <p style="color:white;">Escolha Scan Rápido ou Full Scan</p>
    </td>
    <td style="text-align:center;">
      <img src="https://github.com/Andrey-Soares8/Portscanner/blob/main/src/scan%20feito%20(4).png" alt="Resultado do escaneamento" style="width:90%; border: 1px solid transparent;"/>
      <p style="color:white;">Scan Feito</p>
    </td>
  </tr>
</table>

</div>



Este software deve ser usado apenas para **fins educacionais** e testes em **redes próprias**. ❌ **Não utilize para escanear redes ou sistemas sem autorização**, pois isso pode ser **ilegal** dependendo da legislação local.

