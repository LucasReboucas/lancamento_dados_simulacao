########################################################################################################
# Este arquivo simula "LANCAMENTOS" lancamentos de "DADOS" dados com "LADOS" lados e mostra a frequência dos possiveis resultados obtidos
# Autor: Lucas Rebouças
########################################################################################################

from random import randint
import matplotlib.pyplot as plt
import statistics
import numpy as np


DADOS = 2
LADOS = 6
LANCAMENTOS = 100000



class LancamentosDados(object):
    # construtor do objeto
    def __init__(self, dados, lados, lancamentos):
        self.dados = dados
        self.lados = lados
        self.lancamentos = lancamentos
        self.resultados = []
        self.frequencias = []
        self.soma_minima = self.dados
        self.soma_maxima = self.dados*self.lados
        
    
    # metodo que retorna o resultado do lancamento lancamentos de dados
    def lancar(self):
        lancamentos = self.lancamentos
        
        while(lancamentos >0):
            soma_obtida = 0
            for count in range(self.dados):
                aux = randint(1, self.lados)
                soma_obtida += aux
            self.resultados.append(soma_obtida)
            lancamentos -= 1
            
        for count in range(self.soma_minima, self.soma_maxima + 1):
            self.frequencias.append(self.resultados.count(count))
            
        return [self.resultados, self.frequencias]
    
    
    # metodo que retorna as somas obtidas obtidas ao utilizar o metodo "lancar"
    def obter_resultados(self):
        return self.resultados
    
    
    # metodo que retorna as frequencias obtidas ao utilizar o metodo "lancar"
    def obter_frequencias(self):
        return self.frequencias
    
    
     #Retorna um histograma acrescido de media, mediana e desvio padrao
    def run_histograma(self):        
        freq_media = round(statistics.mean(self.resultados), 2)
        freq_mediana = round(statistics.median(self.resultados), 2)
        freq_desv_pad = round(statistics.stdev(self.resultados), 2)
        esp_amostral = list(range(self.soma_minima, self.soma_maxima+1))
        frequencia = self.frequencias
        titulo_grafico = "Resultado obtido ao jogar " + str(self.dados) + " dado(s) de " + str(self.lados) + " lados " + str(self.lancamentos) + " vez(es)"
        estatisticas = "Estatisticas: " + "Média " + str(freq_media) + "," " Mediana " + str(freq_mediana) + ", Desvio padrão " + str(freq_desv_pad)
        titulo_eixo_y = "Freq. Absoluta"
        titulo_eixo_x = "Resultados"

        plt.bar(esp_amostral, frequencia, width=0.9, alpha=0.6)
        plt.title(titulo_grafico)
        plt.xticks(esp_amostral)
        plt.yticks([]) #remove y axis
        plt.ylim([0, max(frequencia)*1.2]) #set y axis limits
        plt.ylabel(titulo_eixo_y)
        plt.xlabel(titulo_eixo_x)
        for x,y in zip(esp_amostral, frequencia):
            label = frequencia[x-self.dados]
            plt.annotate(label, (x,y), textcoords="offset points", xytext=(0,10), ha='center')
        
        plt.show()
        print(estatisticas)

        return None
    


    
def main():
    jogo = LancamentosDados(DADOS, LADOS, LANCAMENTOS)
    jogo.lancar()
    jogo.run_histograma()

if __name__ == "__main__":
    main()
