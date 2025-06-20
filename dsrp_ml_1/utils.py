import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.preprocessing import StandardScaler

class MachineLearningProcessor:

    def __init__(self, features:list, score:str="", model_type: str = "LinearRegression"):
        self.model_type = model_type
        self.data = joblib.load('../dsrp_ml_1/data/WHR_preprocesado.joblib')
        self.features = features
        self.score = score

    def standarize_data(self):
        # Normaliza los datos
        scaler = StandardScaler()
        self.X_scaled = scaler.fit_transform(self.data[self.features])

    def split_data(self):
        # Seleccionar features (puedes ajustar esto según la matriz de correlación)
        X = self.data[self.features]
        y = self.data[self.score]

        # Dividir en entrenamiento y prueba
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

    def train(self, model_ml):
        if self.model_type == 'KMeans':
            print("1. Normalizando datos")
            self.standarize_data()
            print(f"2. Entrenando model {self.model_type}")
            self.data['Cluster'] = model_ml.fit_predict(self.X_scaled)
            print("3. Entrenamiento finalizado")
        else:
            print("1. Separando datos de train y test..")
            self.split_data()
            print(f"2. Entrenando model {self.model_type}")
            self.fitted_model = model_ml.fit(self.X_train, self.y_train)
            print("3. Entrenamiento finalizado")

    def predict(self):
        self.predictions = self.fitted_model.predict(self.X_test)
        print("R² score:", r2_score(self.y_test, self.predictions))
        print("MSE:", mean_squared_error(self.y_test, self.predictions))

def save(ml_object, name):
    """
    Guarda modelos de ML
    """
    joblib.dump(ml_object, f"../dsrp_ml_1/models/{name}.joblib")
    print("Model guaradado exitosamente")
