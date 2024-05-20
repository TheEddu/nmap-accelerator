import subprocess
import os

# Listas de opções 
def show_nmap_parameters():
    print("PRINCIPAIS PARÂMETROS DO Nmap:")
    print("=========================================================")
    print("{:<10} {:<50}".format("-sS", "Scan TCP SYN (stealth scan)"))
    print("{:<10} {:<50}".format("-sT", "Scan TCP connect"))
    print("{:<10} {:<50}".format("-sU", "Scan UDP"))
    print("{:<10} {:<50}".format("-sV", "Detectar versões dos serviços"))
    print("{:<10} {:<50}".format("-O", "Detectar sistema operacional"))
    print("{:<10} {:<50}".format("-A", "Scan agressivo (Não recomendado)"))
    print("{:<10} {:<50}".format("-Pn", "Não fazer ping antes do scan"))
    print("{:<10} {:<50}".format("-T[0-5]", "Definir tempo de execução"))
    print("=========================================================")    

def show_outputs_options():
    print("OPÇÕES DE SAÍDAS:")
    print("=========================================================")
    print("{:<10} {:<50}".format("-oA <base>", "Salva a saída em três formatos (-oN, -oX, -oG) com uma base de nome"))
    print("{:<10} {:<50}".format("-oN <file>", "Salva a saída normal (plaintext)"))
    print("{:<10} {:<50}".format("-oG <file>", "Salva a saída em formato greppable"))
    print("=========================================================")    

def show_nmap_script_options():
    print("PRINCIPAIS SCRIPTS DO Nmap Scripting Engine (NSE):")
    print("=========================================================")
    print("{:<10} {:<50}".format("auth", "Scripts relacionados à autenticação"))
    print("{:<10} {:<50}".format("broadcast", "Scripts para varreduras de broadcast"))
    print("{:<10} {:<50}".format("brute", "Scripts para força bruta"))
    print("{:<10} {:<50}".format("default", "Scripts padrão do Nmap"))
    print("{:<10} {:<50}".format("discovery", "Scripts de descoberta de informações"))
    print("{:<10} {:<50}".format("dos", "Scripts de negação de serviço"))
    print("{:<10} {:<50}".format("exploit", "Scripts de exploração de vulnerabilidades"))
    print("{:<10} {:<50}".format("external", "Scripts que dependem de recursos externos"))
    print("{:<10} {:<50}".format("fuzzer", "Scripts de fuzzing"))
    print("{:<10} {:<50}".format("intrusive", "Scripts que podem ser intrusivos"))
    print("{:<10} {:<50}".format("malware", "Scripts relacionados a malware"))
    print("{:<10} {:<50}".format("safe", "Scripts considerados seguros para uso"))
    print("{:<10} {:<50}".format("version", "Scripts para detecção de versão de serviços"))
    print("{:<10} {:<50}".format("vuln", "Scripts para detecção de vulnerabilidades"))
    print("=========================================================")

#Definição de input do usuário
def get_user_input():

    #parametros
    show_nmap_parameters()
    options = input("Digite as opções de parâmetros do Nmap (ou pressione Enter para padrão): ")
    #scripts
    use_script = input("Deseja usar algum script do Nmap Scripting Engine (NSE)? (s/n): ").strip().lower()
    script = ''
    if use_script == 's':
        show_nmap_script_options()
        script = input("Digite o nome do script que deseja usar: ").strip()
        options += f" --script={script}"

    #ip
    ip = input("Digite o IP de destino: ")

    #portas
    specify_ports = input("Deseja especificar portas? (s/n): ").strip().lower()
    
    if specify_ports == 's':

        port = input("Digite a porta ou intervalo de portas (exemplo: 80 ou 1-1000): ")
    else:
        port = ''  # Se não especificar portas, deixar em branco

    #output
    save_output = input("Deseja salvar a saída em um arquivo? (s/n): ").strip().lower()

    if save_output == 's':
        show_outputs_options()
        # Pergunta ao usuário o formato de saída
        output_format = input("Escolha o formato de saída (oA, oN, oG): ").strip().lower()
        # Pergunta ao usuário o nome base do arquivo
        output_file = input("Digite o nome base do arquivo de saída (sem extensão): ").strip()
        # Pergunta ao usuário se deseja filtrar a saída -oG
        if output_format == 'og':
            filter_option = input("Deseja filtrar a saída -oG para mostrar somente IPs ou portas? (ips/portas/ambos/none): ").strip().lower()
        else:
            filter_option = 'none'
    else:
        output_format = ''
        output_file = ''
        filter_option = 'none'
    
    return options, ip, port, output_format, output_file, filter_option

#Montagem e execução do comando
def run_nmap(options, ip, port, output_format, output_file, filter_option):

    if port:
        command = f"nmap {options} {ip} -p {port}"
    else:
        command = f"nmap {options} {ip}"

    # Opção de output
    if output_format and output_file:
        if output_format == 'oa':
            command += f" -oA {output_file}"
        elif output_format == 'on':
            command += f" -oN {output_file}"
        elif output_format == 'og':
            command += f" -oG {output_file}.gnmap"

    print(f"\nExecutando comando: {command}")

    result = subprocess.run(command, shell=True, text=True)

    if output_format == 'og' and filter_option in ('ips', 'portas', 'ambos'):
        filter_greppable_output(f"{output_file}.gnmap", filter_option)
    else:
        print(result.stdout)

# Filtro do output
def filter_greppable_output(file_path, filter_option):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        if filter_option == 'ips':
            ips = set()
            for line in lines:
                if line.startswith('Host:'):
                    parts = line.split()
                    ip = parts[1]
                    ips.add(ip)
            with open(f"{file_path}.txt", "w") as f:
                for ip in ips:
                    f.write(ip + "\n")
        
        elif filter_option == 'portas':
            portas = set()
            for line in lines:
                if '/open/' in line:
                    parts = line.split()
                    ip = parts[1]
                    for part in parts:
                        if '/open/' in part:
                            porta = part.split('/')[0]
                            portas.add((ip, porta))
            with open(f"{file_path}.txt", "w") as f:
                for ip, porta in portas:
                    f.write(f"{ip}:{porta}\n")

        elif filter_option == 'ambos':
            ips = set()
            portas = set()
            for line in lines:
                if line.startswith('Host:'):
                    parts = line.split()
                    ip = parts[1]
                    ips.add(ip)
                    for part in parts:
                        if '/open/' in part:
                            porta = part.split('/')[0]
                            portas.add(porta)
            with open(f"{file_path}.txt", "w") as f:
                f.write("IPs encontrados: \n")
                for ip in ips:
                    f.write(ip + "\n")
                f.write("\nPortas encontradas: \n")
                for porta in portas:
                    f.write(porta + "\n")

    except FileNotFoundError:
            print(f"Erro: Arquivo {file_path} não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")                


def main():
    # Obtém o input
    options, ip, port, output_format, output_file, filter_option = get_user_input()
    # Executa o Nmap com as definições escolhidas
    run_nmap(options, ip, port, output_format, output_file, filter_option)

    if output_format == 'og' and os.path.exists(f"{output_file}.gnmap"):
        os.remove(f"{output_file}.gnmap")
        os.rename(f"{output_file}.gnmap.txt", f"{output_file}.txt")

    elif output_format == 'on' and os.path.exists(f"{output_file}.gnmap.txt"):
        os.rename(f"{output_file}.gnmap.txt", f"{output_file}.txt")

    elif os.path.exists(f"{output_file}.gnmap"):
        os.remove(f"{output_file}.gnmap")

    else:
        pass

if __name__ == "__main__":
    main()
