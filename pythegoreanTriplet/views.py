from django.shortcuts import render

# Create your views here.
def lcf(compoundedAmount,principle):
    if principle == 0:
        return compoundedAmount
    return lcf(principle,compoundedAmount % principle)
def calculate_pythegorean_template_v1(request):
    AC = 17
    AB = 8
    BC = 15
    diff = AC - BC
    factor = lcf(AC+AB,BC)
    numerator = int((AC+AB)/factor)
    denominator = int(BC/factor)
    context = {"AC":AC,"AB":AB,"BC":BC,"diff":diff,"factor":factor,"numerator":numerator,"denominator":denominator}
    return render('request','temp1.html',context)

def calculate_pythegorean_template_v2(request):
    AC = 13
    AB = 5
    BC = 12
    diff = AC - BC
    factor = lcf(AC+AB,BC)
    numerator = int((AC+AB)/factor)
    denominator = int(BC/factor)
    context = {"AC":AC,"AB":AB,"BC":BC,"diff":diff,"factor":factor,"numerator":numerator,"denominator":denominator}
    return render('request','temp1.html',context)