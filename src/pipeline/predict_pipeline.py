import pandas as pd
import numpy as np

# Ne pas oublier de changer le mode
from src.utilis import load_object # Ne pas oublier de changer le mode dans utilis.py
from src.components.data_config import AppConfig # Ne pas oublier de changer le mode dans data_config.py


class DataClient:
    def __init__(self):
        """__init__ _summary_
        """
        self.data_preprocessor_model_path = AppConfig()
        self.df_clients= pd.read_csv(self.data_preprocessor_model_path.clients_data__path)
        self.preprocessor= load_object(url_path=self.data_preprocessor_model_path.preprocessor_ob_file__path)
        self.model= load_object(url_path=self.data_preprocessor_model_path.trained_model_file__path)
        self.explainer = load_object(url_path=self.data_preprocessor_model_path.explainer__path)

    def gest_local_explanation(self, df):
        """gest_local_explanation _summary_

        Args:
            df (_type_): _description_

        Returns:
            _type_: _description_
        """
        df = df.replace((np.inf, -np.inf), np.nan).reset_index(drop=True)
        data_scaled= self.preprocessor.transform(df)
        data_scaled = pd.DataFrame(data_scaled, columns= list(df.columns))
        shap_values = self.explainer.shap_values(data_scaled.loc[0])
        test_ = pd.DataFrame(shap_values, index= list(data_scaled.columns), columns=['shape_values'])
        test_ = test_.reset_index()
        test_ = test_.rename(columns={'index': 'Features'})
        test_['features_importance_abs'] = test_['shape_values'].apply(abs)
        #test_ = test_.sort_values(by="features_importance_abs", ascending=False, inplace=True)
        return test_

    def liste_id_clients(self):
        """liste_id_clients _summary_

        Returns:
            _type_: _description_
        """
        return self.df_clients.SK_ID_CURR.unique()

    def liste_columns(self):
        """liste_columns _summary_

        Returns:
            _type_: _description_
        """
        return self.df_clients.columns

    def get_data_as_df(self, ID_client):
        """get_data_as_df _summary_

        Args:
            ID_client (_type_): _description_

        Returns:
            _type_: _description_
        """
        ID_client = int(ID_client)
        df_client= (self.df_clients.loc[self.df_clients["SK_ID_CURR"] == ID_client]).copy()
        df_client = df_client.drop(["SK_ID_CURR"], axis=1)
        return df_client

    def predict_function(self, df):
        """predict_function _summary_

        Args:
            df (_type_): _description_

        Returns:
            _type_: _description_
        """
        df = df.replace((np.inf, -np.inf), np.nan).reset_index(drop=True)
        data_scaled= self.preprocessor.transform(df)
        data_scaled = pd.DataFrame(data_scaled, columns= list(df.columns))
        # pred= self.model.predict(data_scaled)
        pred= self.model.predict_proba(data_scaled)
        # predicted_classe = pred[0]
        return {"solvable": bool(pred[0][0] > 0.5), "seuil": 0.5, "proba" : pred[0][0]}
