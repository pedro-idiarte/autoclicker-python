# 🖱️ Simple Python Autoclicker

Um autoclicker leve e simples desenvolvido em Python, ideal para automatizar cliques do mouse em uma posição fixa.

## ✨ Funcionalidades

*   **Controle Total:** Inicie, pause e encerre o autoclicker usando teclas de atalho.
*   **Posição Fixa:** Define o ponto de clique na posição atual do mouse.
*   **Não Bloqueante:** Utiliza *threading* para garantir que o programa possa clicar e, ao mesmo tempo, escutar comandos do teclado.
*   **Fácil de Usar:** Interface de linha de comando minimalista e intuitiva.

## 🛠️ Requisitos

*   **Python 3** (Recomendado 3.6+)
*   Sistema Operacional: Windows, macOS ou Linux.

## 📦 Instalação

O projeto depende da biblioteca `pynput`, que permite o controle de mouse e teclado.

1.  **Clone o Repositório** (Se estiver no GitHub):
    ```bash
    git clone https://github.com/seu-usuario/simple-python-autoclicker.git
    cd simple-python-autoclicker
    ```

2.  **Instale a Dependência:**
    ```bash
    pip install pynput
    ```

## 🚀 Como Usar

O script `autoclicker.py` utiliza as teclas **F6** e **ESC** para controle.

1.  **Execute o Script:**
    ```bash
    python autoclicker.py
    ```

2.  **Instruções Iniciais:** O console exibirá as instruções de uso:

    ```
    --- Autoclicker Simples em Python ---
    Instruções:
    1. Posicione o mouse no local desejado para o clique.
    2. Pressione a tecla F6 para definir a posição e INICIAR o autoclick.
    3. Pressione F6 novamente para PAUSAR o autoclick.
    4. Pressione a tecla ESC a qualquer momento para ENCERRAR o programa.
    --------------------------------------
    ```

3.  **Iniciar o Autoclick:**
    *   Mova o cursor do mouse para o local da tela onde você deseja que os cliques automáticos ocorram.
    *   Pressione a tecla **F6**. O script registrará a posição e começará a clicar.

4.  **Pausar/Retomar:**
    *   Pressione **F6** novamente para pausar o autoclick.
    *   Pressione **F6** mais uma vez para retomar o autoclick na mesma posição.

5.  **Encerrar o Programa:**
    *   Pressione a tecla **ESC** para parar o autoclick e fechar o programa.

## ⚙️ Configuração (Opcional)

Você pode ajustar a velocidade de clique editando o arquivo `autoclicker.py`.

Procure pela linha:

```python
time.sleep(0.05) # 20 cliques por segundo
```

Altere o valor `0.05` para um novo intervalo em segundos. Por exemplo, para clicar a cada 1 segundo, use `time.sleep(1)`.
