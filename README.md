# ScriptBKP-Android-PC-Pendrive
<br>
Este script foi desenvolvido para realizar o backup de fotos do celular para o PC e, em seguida, transferir o backup completo do PC para um pendrive.

Ele orquestra a interação entre múltiplas plataformas: **um PC com Windows, um celular Android e um dispositivo de armazenamento externo (pendrive)**, facilitando o processo de backup e transferência de dados entre sistemas heterogêneos.
<br>
<br>
## Fluxo Geral
1. O backup anterior das fotos no PC é removido.
2. As fotos mais recentes do celular são copiadas para o PC.
3. O backup completo do PC (incluindo as fotos copiadas) é transferido para o pendrive.


## Requisitos e Pré-Requisitos
1. O script utiliza a ferramenta **ADB (Android Debug Bridge)** para interagir com dispositivos Android a partir do Python. Portanto, é necessário instalá-la no PC.
<a rel="noopener" target="_new" href="https://developer.android.com/tools/releases/platform-tools?hl=pt-br" style="--streaming-animation-state: var(--batch-play-state-1); --animation-rate: var(--batch-play-rate-1);"><span style="--animation-count: 1; --streaming-animation-state: var(--batch-play-state-2);">Baixar</span><span style="--animation-count: 2; --streaming-animation-state: var(--batch-play-state-2);"> ADB</span></a>

2. Antes de executar o script:

    * Certifique-se de que o celular está conectado ao PC via USB, com a **depuração USB ativada** (encontrada geralmente nas opções de desenvolvedor).
    * O pendrive deve estar plugado, formatado, e com uma nova pasta criada para receber o backup.
<br>
<br>

## Observações Adicionais
1. **Caminhos de diretórios:**

    * Para diretórios Windows, utilize barras invertidas (\\), exemplo: C:\nome\pasta.
    * Para diretórios no Android, use barras normais (/), exemplo: /sdcard/nome/pasta.

2. O script e o Windows são sensíveis à nomenclatura de pastas e diretórios. **Evite usar espaços e caracteres especiais** nos nomes dos diretórios para evitar erros.

## Sistemas e Ferramentas Utilizados
* **Sistema Operacional (PC)**: Windows 10 Pro, versão 22H2
* **Sistema Operacional (Celular)**: Xiaomi MIUI 14.0.3, Android 12 SKQ1
* **Python**: versão 3.10.7
* **Pip**: versão 24.2 (gerenciador de pacotes Python)
* **ADB**: versão 1.0.41

## Sobre a Formatação de Pendrives
* **NTFS**: Restrito ao Windows (Microsoft), recomendado para grandes volumes de dados, mas não compatível com muitos dispositivos fora do ambiente Windows.
* **FAT32**: Sistema mais antigo, aceita arquivos de até 4GB. Compatível com a maioria dos dispositivos, mas limitado por esse tamanho de arquivo.
* **exFAT**: Uma versão atualizada do FAT32, aceita arquivos maiores que 4GB e é amplamente suportado por dispositivos mais recentes.
<br>
<br>

## Após rodar o script, o terminal retorna:
![terminal_script](https://github.com/user-attachments/assets/935ae22b-e751-4f41-934d-f7f6283982c0)

