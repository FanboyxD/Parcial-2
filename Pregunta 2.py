class Permutaciones(object):
    def __init__(self):
        pass
    def permu(self,n,x):
        if isinstance(n>=x)and isinstance(n,int)and isinstance(x,int):
            return self.permu_aux(n,x,0,0)/x
        else:return "Error"
    def permu_aux(self,n,x,contador,result):
        if n-contador==1:
            return result
        elif n - contador>1:
            return self.permu_aux(n*(n-contador),x,contador+1,result+n)
        elif x-contador > 1:
            return self.permu_aux(n,((n-x)*((n-x)-contador)),contador,result+n)
        else:return self.permu_aux(n,x,contador-1,result+n)
