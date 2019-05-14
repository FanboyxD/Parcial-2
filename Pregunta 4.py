class Barras(object):
    def __init__(self):
        pass
    def barras(self,lista):
        if isinstance(lista,list):
            return self.barras_aux(lista,0,0,[])
        else:return "Error"
    def barras_aux(self,lista,fila,col,matriz):
        if fila==len(lista):
            return matriz
        elif col==len(matriz[0]):
            return self.barras_aux(lista,fila+1,0,matriz)
        elif col<len(matriz[0]):
            return self.barras_aux(lista,fila,col+1,matriz)
        else:return self.barras_aux(lista,fila,col,matriz+[fila][col])
