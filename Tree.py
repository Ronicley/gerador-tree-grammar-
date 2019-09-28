class No:
    def __init__(self, valor):
        self.info = valor
        self.esq = None
        self.centro = None
        self.dir = None

    def insereEsq(self, valor):
        self.esq = No(valor)

    def insereCentro(self, valor):
        self.centro = No(valor)

    def insereDir(self, valor):
        self.dir = No(valor)

    def insere(self, valor):
        if valor < self.info:
            if self.esq == None:
                self.esq = No(valor)

            else:
                self.esq.insere(valor)
        else:
            if self.dir == None:
                self.dir = No(valor)

            else:
                self.dir.insere(valor)


    def inOrdem(self):
        if self.centro != None:
            self.centro.inOrdem()
        if self.esq != None:
            self.esq.inOrdem()
        print(self.info, end=" ")
        if self.dir != None:
            self.dir.inOrdem()






class Tree:
    def __init__(self):
        self.raiz = None

    def insereEsq(self, valor):
        if self.raiz == None:
            self.raiz = No(valor);

        else:
            self.raiz.insereEsq(valor)

    def insereDir(self, valor):
        if self.raiz == None:
            self.raiz = No(valor);

        else:
            self.raiz.insereDir(valor)

    def insereCentro(self, valor):
        if self.raiz == None:
            self.raiz = No(valor);

        else:
            self.raiz.insereCentro(valor)


    def insere(self, valor):
        if self.raiz == None:
            self.raiz = No(valor);

        else:
            self.raiz.insere(valor)

    def inOrdem(self):
        if self.raiz != None:
            self.raiz.inOrdem()



