import warnings # silencia avisos innecesarios
warnings.filterwarnings("ignore") # matplotlib necesita esta línea ANTES de cualquier import de pyplot # para que IDLE pueda abrir ventanas de gráficas
import matplotlib
matplotlib.use("TkAgg") # ← obligatorio para IDLE
import matplotlib.pyplot as plt
import numpy as np # ── HERRAMIENTAS DE SCIKIT-LEARN zamorano valero alejandra
from sklearn.datasets import load_breast_cancer # el dataset from sklearn.model_selection import train_test_split # dividir datos from sklearn.ensemble import RandomForestClassifier # el modelo from sklearn.metrics import ( accuracy_score, # % de aciertos totales precision_score, # de lo que predije +, ¿cuánto era +? recall_score, # de todos los + reales, ¿cuántos encontré? f1_score, # media armónica de precision y recall confusion_matrix, # tabla TP/TN/FP/FN classification_report # reporte completo )
print("✅ Paso 1 completado — librerías cargadas correctamente")
