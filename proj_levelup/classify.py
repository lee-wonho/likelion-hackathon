import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj_levelup.settings')
import django
django.setup()

from interpark import scrap_interpark, result_interpark

def integrate_ex_pr(ex_pr1, ex_pr2):
    result_ex_pr = ex_pr1 + ex_pr2
    
    return result_ex_pr

def integrate_sh_con(sh_con1, sh_con2):
    result_sh_con = sh_con1 + sh_con2
    
    return result_sh_con

def integrate_th_mu(th_mu1, th_mu2):
    result_th_mu = th_mu1 + th_mu2
    
    return result_th_mu

# dict_inter = scrap_interpark()
# ex_pr_inter, sh_con_inter, th_mu_inter = result_interpark(dict_inter)
# ex_pr_yes24, sh_con_yes24, th_mu_yes24 = result_interpark(dict_inter)

# print(ex_pr_inter)
# print("\n")
# print(sh_con_inter)
# print("\n")
# print(th_mu_inter)

# result_ex_pr = ex_pr(ex_pr_inter, ex_pr_yes24)
# print(result_ex_pr)

# result_sh_con = sh_con(sh_con_inter, sh_con_yes24)
# print(result_sh_con)

# result_th_mu = th_mu(th_mu_inter, th_mu_yes24)
# print(result_th_mu)