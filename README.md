# Nmap Accelerator

O Nmap Accelerator é um script Python desenvolvido por mim, um estudante de Segurança da informação, para facilitar o uso do Nmap. Este script permite que os usuários configurem e executem varreduras de rede de maneira rápida e eficiente, oferecendo opções para definir parâmetros de varredura, especificar portas, utilizar scripts do Nmap Scripting Engine (NSE) e salvar resultados em diferentes formatos de saída.

## Como Funciona
O Nmap Accelerator é executado a partir da linha de comando. Ele solicita ao usuário as opções desejadas de parâmetros de varredura, scripts do NSE, endereço IP de destino, portas a serem escaneadas e opções de saída. Com base nessas entradas, o script constrói e executa o comando Nmap correspondente usando a biblioteca subprocess do Python.

Após a conclusão da varredura, o script pode filtrar a saída do Nmap, se desejar. Por exemplo, é possível extrair apenas os IPs ou as portas abertas encontradas durante a varredura e salvá-los em arquivos separados.

## Principais Recursos
Facilidade de uso: Interface intuitiva para personalizar as varreduras do Nmap. Com a exibição das opções, não é preciso ficar presquisando pelos (principais) parametros ou scripts que não se lembrar.

Opções de saída flexíveis: Salve a saída da varredura em diferentes formatos.

Filtragem de resultados: Extraia apenas as informações relevantes dos resultados da varredura para análise posterior.

## Funcionalidades

O script oferece as seguintes funcionalidades:

- **Seleção de Parâmetros do Nmap:** Os usuários podem escolher os parâmetros do Nmap, incluindo diferentes tipos de varredura, detecção de versões de serviços e sistemas operacionais, e configurações de tempo de execução.

- **Utilização de Scripts do NSE:** Os usuários têm a opção de utilizar os scripts disponíveis no Nmap Scripting Engine (NSE), que oferecem funcionalidades adicionais para detecção de vulnerabilidades, exploração de serviços e muito mais.

- **Especificação de Portas:** Os usuários podem especificar portas individuais ou intervalos de portas para varredura, permitindo uma personalização completa do escopo da varredura.

- **Opções de Saída Flexíveis:** O script oferece opções para salvar os resultados da varredura em diferentes formatos, incluindo texto simples, XML e formato greppable, com a capacidade de filtrar e extrair informações específicas, como IPs e portas abertas.

## Como Usar

Para usar o Nmap Accelerator, siga estas etapas:

1. **Clone o Repositório:** Baixe ou clone o repositório para o seu ambiente local.

2. **Execute o Script:** Execute o script `nmaccelerator.py` em um terminal Python compatível.

3. **Siga as Instruções:** Siga as instruções fornecidas pelo script para selecionar parâmetros de varredura, especificar o IP de destino, definir portas de interesse e escolher opções de saída.

4. **Analise os Resultados:** Após a conclusão da varredura, analise os resultados salvos nos arquivos de saída especificados.

## AVISO LEGAL/DISCLAIMER E AMBIENTE DE TESTES

Este script foi desenvolvido por um estudante para praticar e para fins educacionais e de testes. Foi testado em um ambiente controlado do TryHackMe para garantir sua funcionalidade e compatibilidade com o Nmap. Se você encontrar problemas ou tiver dúvidas sobre o uso do script, sinta-se à vontade para relatar problemas ou entrar em contato para obter suporte adicional.
Não é destinado a ser utilizado para fins maliciosos ou ilegais. O uso deste script em ambientes de produção ou em redes que você não tem permissão para escanear pode violar leis ou políticas de segurança. Sempre obtenha permissão adequada antes de realizar varreduras de rede em qualquer ambiente.
