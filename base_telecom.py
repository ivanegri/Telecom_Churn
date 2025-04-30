import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()

np.random.seed(42)
random.seed(42)

data = {
    "cliente_id": [f"C{1000 + i}" for i in range(1000)],
    "idade": np.random.randint(18, 80, 1000),
    "sexo": np.random.choice(["Masculino", "Feminino"], 1000),
    "tempo_contrato_meses": np.random.randint(1, 72, 1000),
    "servico_internet": np.random.choice(["Fibra", "DSL", "Não tem"], 1000, p=[0.5, 0.3, 0.2]),
    "tipo_contrato": np.random.choice(["Mensal", "Anual", "Bianual"], 1000, p=[0.6, 0.3, 0.1]),
    "valor_mensal": np.round(np.random.uniform(20, 120, 1000), 2),
    "total_gasto": lambda x: np.round(x.tempo_contrato_meses * x.valor_mensal * np.random.uniform(0.9, 1.1), 2),
    "num_servicos": np.random.randint(1, 5, 1000),
    "dependentes": np.random.choice(["Sim", "Não"], 1000, p=[0.3, 0.7]),
    "fatura_online": np.random.choice(["Sim", "Não"], 1000, p=[0.7, 0.3]),
    "seguro_dispositivo": np.random.choice(["Sim", "Não"], 1000, p=[0.4, 0.6]),
    "suporte_tecnico": np.random.choice(["Sim", "Não"], 1000, p=[0.4, 0.6]),
    "churn": np.random.choice(["Sim", "Não"], 1000, p=[0.3, 0.7])
}

df = pd.DataFrame(data)
df["total_gasto"] = df.tempo_contrato_meses * df.valor_mensal * np.random.uniform(0.9, 1.1, 1000)
df["total_gasto"] = df["total_gasto"].round(2)

for col in ["seguro_dispositivo", "suporte_tecnico"]:
    df.loc[df.sample(frac=0.05).index, col] = np.nan

df.to_csv("telecom_churn_data.csv", index=False)