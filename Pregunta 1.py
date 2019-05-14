class Asterisco(object):
    def __init__(self):
        pass
    def masterisco(self,n):
        if isinstance(n,int):
            return self.masterisco_aux(n,0,0,[],0)
        else:return "Error"
    def masterisco_aux(self,fila,col,result,resta):
        if fila == n:
            return result
        elif col == n:
            return self.masterisco_aux(n,fila+1,0,result,resta)
        elif fila < n:
            return self.masterisco_aux(n,fila,col+1,result,resta)
        elif n-resta > 0:
            return (self.masterisco_aux(n,fila,col,result+((n-resta)+str"*"),
                                        resta+1))
        else:return self.masterisco_aux(n,fila,col,result,resta)
