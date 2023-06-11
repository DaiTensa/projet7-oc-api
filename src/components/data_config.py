
import os
from dataclasses import dataclass

##############################APP DATA PATH CONFIG ####################################################################
########################################SERVER##########################################################################

@dataclass
class AppConfig:
    clients_data__path: str=os.path.join("https://raw.githubusercontent.com/DaiTensa/dashboard/main/", "reduced_test.csv")
    preprocessor_ob_file__path: str=os.path.join("https://raw.githubusercontent.com/DaiTensa/dashboard/main/", "preprocessor_best_model.pkl")
    trained_model_file__path: str=os.path.join("https://raw.githubusercontent.com/DaiTensa/dashboard/main/", "LogisticRegression.pkl")
    explainer__path: str=os.path.join("https://raw.githubusercontent.com/DaiTensa/dashboard/main/", "Explainer_LogesticRegression.pkl")

# Pour RUN l'api en local incomment à partir de la ligne 18 et comment ligne 8 -> ligne 13
##############################APP DATA PATH CONFIG ####################################################################
########################################LOCAL##########################################################################
# @dataclass
# class AppConfig:
#     clients_data__path: str=os.path.join('C:/Users/Lenovo/Documents/DSPython/data_projet_7/', "Final_test_df.csv")
#     preprocessor_ob_file__path: str=os.path.join('C:/Users/Lenovo/Documents/DSPython/projetscoring/notebook/artifacts/', "preprocessor_best_model.pkl")
#     trained_model_file__path: str=os.path.join("C:/Users/Lenovo/Documents/DSPython/projetscoring/notebook/artifacts/", "best_model_pretrained.pkl")
#     explainer__path: str=os.path.join("C:/Users/Lenovo/Documents/DSPython/projetscoring/notebook/artifacts/", "Explainer_LogReg.pkl")
