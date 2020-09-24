from django.shortcuts import render
from scrap_interpark import result_interpark

# Create your views here.

ex_pr_inter, sh_con_inter, th_mu_inter = result_interpark()
ex_pr_yes24, sh_con_yes24, th_mu_yes24 = result_interpark()

def ex_pr(request): 
    result_ex_pr = (ex_pr_inter + ex_pr_yes24)
    # print(result_ex_pr)
    

    return render(request, 'ex_pr.html', {'result_ex_pr' : result_ex_pr})

# def sh_con(request):  
#     result_sh_con = (sh_con_inter + sh_con_yes24)
#     print(result_sh_con)

#     return render(request, 'sh_con.html', {'result_sh_con' : result_sh_con})

# def th_mu(request):  
#     result_th_mu = (th_mu_inter + th_mu_yes24)
#     print(result_th_mu)

#     return render(request, 'th_mu.html', {'result_th_mu' : result_th_mu})

