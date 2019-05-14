class Magico(object):
    def __init__(self):
        pass
    def es_magico(self,matriz):
        if isinstance(matriz,list):
            return self.magico_aux(matriz,0,0,[])
        else:return "Error"
    def magico_aux(self,matriz,fila,col,result):
        if fila==len(matriz):
            return True
        elif col==len(matriz[0]):
            return self.magico_aux(matriz,fila+1,0,result)
        elif col<len(matriz[0]):
            return self.magico_aux(matriz,fila,col+1,result)
        else:return False
