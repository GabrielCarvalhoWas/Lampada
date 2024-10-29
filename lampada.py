import time
from enum import Enum

class EstadoLampada(Enum):
    ON = "on"
    OFF = "off"

class Lampada:
    def __init__(self, estado, local):
        self.brilho = "medio"
        self.estado = estado
        self.local = local
        self.historico = []
    
    def exibir_estado(self):
        print(f"Estado da lampada:  {self.local} - {self.estado.value} - Brilho: {self.brilho}")
    
    def ligar_lampada(self):
        if self.estado == EstadoLampada.ON:
            print("A lampada ja esta ligada.")
        else:
            print(f"Ligando a lampado....")
            for i in range(1, 4):
                print(f"{i} segundo(s)...")
                time.sleep(1)
            print("Lampada Ligada!!!")
            self.estado = EstadoLampada.ON
            self.historico.append("Ligada")

    
    def desligar_lampada(self):
        if self.estado == EstadoLampada.OFF:
            print("A lampada ja esta desligada.")
        else:
            print("Desligando a lâmpada...")
            for i in range(1, 4):
                print(f"{i} segundo(s)...")
                time.sleep(1)
            print("Lâmpada desligada!")
            self.estado = EstadoLampada.OFF
            self.historico.append("Desligada")


    def ajuste_brilho(self, brilho_novo):
        if brilho_novo in ["baixo","medio","alto"]:
            self.brilho = brilho_novo
            print(f"Brilho ajustado para {self.brilho}")
        else:
            print("Nível de brilho inválido. Escolha 'baixo', 'médio' ou 'alto'.")

    
    def controle_usuario(self):
        while True:
            usuario = str(input("Deseja ligar, desligar ou ajustar o brilho da  lampada ? [on/off/brilho]: ")).strip().lower()
            if usuario == "on":
                self.ligar_lampada()
                break
            elif usuario == "off":
                self.desligar_lampada()
                break
            elif usuario == "brilho":
                while True:
                    b = str(input("Escolha o nivel de brilho de preferencia [baixo/medio/alto]: ")).strip().lower()
                    if b in ['baixo', 'medio', 'alto']:
                        self.ajuste_brilho(b)
                        break
                    else:
                        print("Nível de brilho inválido. Por favor, escolha 'baixo', 'médio' ou 'alto'.")
            else:
                print(f"Ação inválida. Por favor, escolha 'on' ou 'off' ou 'brilho'.")

            
        while True:  
            opcao = str(input("Deseja continuar ? [sim/nao]: ")).strip().lower()
            if opcao == 'sim':
                self.controle_usuario()
                break
            elif opcao == 'nao':
                print("Programa encerrado.")
                break
            else:
                print("Resposta inválida. Por favor, escolha 'sim' ou 'nao'.")


lampada1 = Lampada(EstadoLampada.OFF,"Quarto")
lampada1.exibir_estado()
lampada1.controle_usuario()
lampada1.exibir_estado()
