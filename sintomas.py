def calcular_bayes(prior_A, probabilidad_B_Dado_A, probabilidad_B):
    return (prior_A * probabilidad_B_Dado_A) / probabilidad_B

if __name__ == "__main__":
    prob_cancer = 1 / 100000
    prob_sintoma_dado_cancer = 1
    prob_sintoma_dado_no_cancer = 10 / 99999
    porb_no_cancer = 1 - prob_cancer

    prob_sintoma = (prob_sintoma_dado_cancer * prob_cancer) + (prob_sintoma_dado_no_cancer * porb_no_cancer)

    prob_cancer_dado_sintoma = calcular_bayes(prob_cancer, prob_sintoma_dado_cancer, prob_sintoma)
    print(prob_cancer_dado_sintoma)