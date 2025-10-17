from django.shortcuts import render

# Create your views here.
def lcf(compoundedAmount,principle):
    if principle == 0:
        return compoundedAmount
    return lcf(principle,compoundedAmount % principle)
def calculate_pythegorean_template_v1(request):
    hypotenuse = 17
    perpendicular = 8
    base = 15
    hypotenuse_base = hypotenuse - base
    factor = lcf(hypotenuse+perpendicular,base)
    numerator = int((hypotenuse+perpendicular)/factor)
    denominator = int(base/factor)
    context = {"hypotenuse":hypotenuse,"perpendicular":perpendicular,"base":base,"hypotenuse_base":hypotenuse_base,"factor":factor,"numerator":numerator,"denominator":denominator}
    return render('request','temp1.html',context)

def calculate_pythegorean_template_v2(request):
    hypotenuse = 13
    perpendicular = 5
    base = 12
    hypotenuse_base = hypotenuse - base
    factor = lcf(hypotenuse+perpendicular,base)
    numerator = int((hypotenuse+perpendicular)/factor)
    denominator = int(base/factor)
    context = {"hypotenuse":hypotenuse,"perpendicular":perpendicular,"base":base,"hypotenuse_base":hypotenuse_base,"factor":factor,"numerator":numerator,"denominator":denominator}
    return render('request','temp1.html',context)