from django.shortcuts import render

# Create your views here.
def lcf(compoundedAmount,principle):
    if principle == 0:
        return compoundedAmount
    return lcf(principle,compoundedAmount % principle)

def calculate_interest_v1(request): 
    principle = 8000
    compoundedAmount = 9856
    years = 3
    factor = lcf(compoundedAmount,principle)
    reducedPrinciple = int(principle/factor)
    reducedCompoundAmount = int(compoundedAmount/factor)
    x = int(reducedCompoundAmount **(1/years))
    y = int(reducedPrinciple ** (1/years))
    change_x = x-y
    r = int((change_x/y)*100)
    reducedYears = years-1
    reducedYearsCompoundAmount = int(principle * (1 + (r / 100)) ** reducedYears)
    context = {"principle":principle,"compoundAmount":compoundedAmount,"factor":factor,"years":years,"reducedPrinciple":reducedPrinciple,"reducedCompoundAmount":reducedCompoundAmount,'x':x,'y':y,"change_x":change_x,'r':r,'reducedYears':reducedYears,'reducedYearsCompoundAmount':reducedYearsCompoundAmount,'range':range(reducedYears)}
    return render(request, "interestcompounded.html",context)

def calculate_interest_v2(request): 
    principle = 5000
    compoundedAmount = 6050
    years = 2
    factor = lcf(compoundedAmount,principle)
    reducedPrinciple = int(principle/factor)
    reducedCompoundAmount = int(compoundedAmount/factor)
    x = int(reducedCompoundAmount **(1/years))
    y = int(reducedPrinciple ** (1/years))
    change_x = x-y
    r = int((change_x/y)*100)
    reducedYears = years-1
    reducedYearsCompoundAmount = int(principle * (1 + (r / 100)) ** reducedYears)
    context = {"principle":principle,"compoundAmount":compoundedAmount,"factor":factor,"years":years,"reducedPrinciple":reducedPrinciple,"reducedCompoundAmount":reducedCompoundAmount,'x':x,'y':y,"change_x":change_x,'r':r,'reducedYears':reducedYears,'reducedYearsCompoundAmount':reducedYearsCompoundAmount,'range':range(reducedYears)}
    return render(request, "interestcompounded.html",context)