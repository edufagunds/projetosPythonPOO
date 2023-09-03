import re

# Aqui estou criando a classe que fará todo o processo do outro arquivo
class ExtratorURL:
    def __init__(self, url):
        self.url = self.tratamento_url(url)
        self.valida_url()
    
    # apos receber a url ele irá retirar todos os espaços em branco
    # essa funcao ira verificar tambem se o valor da url é verdadeiro ou falso
    def tratamento_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''
    
    # ele nao recebe a url como parametro, pois irá acessar a propria instancia
    # aqui estou criando a mensagem de erro, caso a url seja vazia
    # not self url, ou seja, o valor não é verdadeiro
    # insiro tambem um metodo de regex para validar a URL
    def valida_url(self):
        if not self.url:
            raise ValueError('A URL esta vazia')
        
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError('A URL nao é valida')
            
        
    # encontrar o caractere na url e fatiar do ponto zero até ele
    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base
    # mesmo esquema, porem agora pegar o caractere, acrescentar mais um e fatiar até o fim
    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao+1:]
        return url_parametros
    
    #aqui especifico o valor da variavel que quero trazer
    #se eu colocar quantidade ele trará 100
    #se colocar moedaOrigem, trará real
    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)

        indice_valor = indice_parametro + len(parametro_busca) + 1

        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)

        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)
    
    def __str__(self):
        return self.url + '\n' + 'Parametros: ' + self.get_url_parametros() + '\n' + 'URL Base: ' + self.get_url_base()
    
    def __eq__(self, other):
        return self.url == other.url

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator = ExtratorURL(url)
valor_quantidade = extrator.get_valor_parametro('quantidade')
print(valor_quantidade)

dolar = 5.5
moeda_origem = extrator.get_valor_parametro('real')
moeda_destino = extrator.get_valor_parametro('dolar')

if moeda_origem == 'real':
    real_para_dolar = float(valor_quantidade) / dolar
    print(real_para_dolar)
if moeda_origem == 'dolar':
    dolar_para_real = float(valor_quantidade) * dolar
    print(dolar_para_real)