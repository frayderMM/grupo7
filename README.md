# 🏠 Sistema de Predicción de Precios de Vivienda

Sistema completo con modelo LightGBM + Feature Engineering, API FastAPI y Frontend Web.

## 📋 Archivos del Proyecto

- `features.py` - Función de Feature Engineering
- `api.py` - API FastAPI para predicciones
- `index.html` - Página web para usar el modelo
- `save_model.py` - Script para guardar tu modelo
- `requirements.txt` - Dependencias del proyecto

## 🚀 Pasos para Ejecutar

### 1️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

### 2️⃣ Guardar tu modelo

Abre `save_model.py`, agrega tu código de entrenamiento y ejecuta:

```python
# Al final de tu código de entrenamiento:
import joblib
joblib.dump(best_model, "model.pkl")
print("✅ Modelo guardado como model.pkl")
```

O directamente en tu notebook/script de entrenamiento.

### 3️⃣ Iniciar la API

```bash
uvicorn api:app --reload
```

La API estará disponible en: `http://127.0.0.1:8000`

### 4️⃣ Abrir la página web

Simplemente abre `index.html` en tu navegador.

## 📊 Uso

1. Ingresa los datos de la vivienda en el formulario
2. Haz clic en "Predecir Precio"
3. Obtén el precio estimado instantáneamente

## 🔧 API Endpoints

- `GET /` - Información de la API
- `POST /predict` - Realizar predicción

### Ejemplo de request:

```
POST http://127.0.0.1:8000/predict?income=75000&age=5.5&rooms=7&bedrooms=4&population=35000
```

## 📝 Notas

- Asegúrate de que `model.pkl` esté en el directorio del proyecto
- La API debe estar corriendo antes de usar el frontend
- El modelo usa las mismas features de ingeniería que entrenaste
