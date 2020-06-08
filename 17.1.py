import numpy

for k in [5,20,50,500]:
    a = 0
    for i in range(5000):
        x = numpy.random.randn(k)
        y = numpy.random.randn(k)
        a += numpy.corrcoef(x,y)[0,1]
    print(k,": ", a/100)
