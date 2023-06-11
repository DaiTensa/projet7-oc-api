from flask import Flask
from src.pipeline.predict_pipeline import DataClient
import json
from numba.core.errors import NumbaDeprecationWarning, NumbaPendingDeprecationWarning
import warnings

warnings.simplefilter('ignore', category=NumbaDeprecationWarning)
warnings.simplefilter('ignore', category=NumbaPendingDeprecationWarning)

# Initiation de l'app flask
app = Flask(__name__)
# Importation des data + model + preprocessor + explainer
data_clients = DataClient()

# route : data client une ligne + columns
@app.route('/data/<int:id_client>', methods=['GET'])
def results_json(id_client):
    """results_json _summary_

    Args:
        id_client (_type_): _description_

    Returns:
        _type_: _description_
    """
    df_client = data_clients.get_data_as_df(ID_client= int(id_client))
    data_json = df_client.to_json(indent=4)
    return data_json

# route : proba solvable insolvable
@app.route('/proba/<int:id_client>', methods=['GET'])
def prediction(id_client):
    """prediction _summary_

    Args:
        id_client (_type_): _description_

    Returns:
        _type_: _description_
    """
    # id_client = requests.args['id_client']
    df_client = data_clients.get_data_as_df(ID_client= int(id_client))
    pred = data_clients.predict_function(df_client)
    return json.dumps(pred, indent=4)

# route : liste des id client
@app.route('/listeidclients', methods=['GET'])
def liste_id_clients():
    """liste_id_clients _summary_

    Returns:
        _type_: _description_
    """
    liste_ids = data_clients.liste_id_clients()
    liste_ids = liste_ids.tolist()
    return json.dumps(liste_ids)

# route: liste noms de colonnes
@app.route('/listecolumnsnames', methods=['GET'])
def liste_columns_names():
    """liste_columns_names _summary_

    Returns:
        _type_: _description_
    """
    liste_columns = data_clients.liste_columns()
    liste_columns = liste_columns.tolist()
    return json.dumps(liste_columns)

# route: shap values
@app.route('/shape/<int:id_client>', methods=['GET'])
def get_shap_values(id_client):
    """get_shap_values _summary_

    Args:
        id_client (_type_): _description_

    Returns:
        _type_: _description_
    """
    df_client = data_clients.get_data_as_df(ID_client= int(id_client))
    shape_val = data_clients.gest_local_explanation(df_client)
    # arr_str = np.array2string(shape_val, separator=',')
    shape_val_json = shape_val.to_json(indent=4)
    return shape_val_json

if __name__ == "__main__":
    app.run(debug=True)