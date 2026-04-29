# 📖 Manual de Usuario – Analizador de Fortaleza de Contraseñas

## ¿Qué es este programa?

El Analizador de Fortaleza de Contraseñas es una herramienta que te permite saber qué tan segura es una contraseña. El programa la evalúa y te dice si es débil, moderada o fuerte, y qué podés hacer para mejorarla.

---

## ⚙️ Requisitos previos

- Tener **Python 3.8 o superior** instalado en tu computadora
- Sistema operativo: Windows, macOS o Linux

Para verificar si tenés Python instalado, abrí una terminal y escribí:
```bash
python --version
```

---

## 📥 Instalación

1. Descargá el archivo `analizador.py` desde este repositorio
   - Hacé clic en el archivo → botón **"Download raw file"**
2. Guardalo en una carpeta de tu elección, por ejemplo: `C:\Usuarios\TuNombre\analizador`

---

## ▶️ Cómo ejecutar el programa

1. Abrí la terminal de tu sistema operativo
   - **Windows:** buscá "cmd" o "PowerShell" en el menú inicio
   - **Mac/Linux:** abrí la aplicación "Terminal"
2. Navegá hasta la carpeta donde guardaste el archivo:
```bash
cd C:\Usuarios\TuNombre\analizador
```
3. Ejecutá el programa:
```bash
python analizador.py
```

---

## 🖥️ Uso del programa

Al ejecutar el programa, verás la siguiente pantalla:
=============================================
ANALIZADOR DE FORTALEZA DE CONTRASEÑAS
Ingresá una contraseña (o 'salir' para terminar):

Simplemente **escribí tu contraseña y presioná Enter**.

### Ejemplo de resultado:
Puntaje: 6/7
Fortaleza: FUERTE 🟢
Recomendaciones:
→ Incluí al menos un símbolo especial (!@#$%...).

### Para analizar otra contraseña:
Simplemente escribí la siguiente contraseña cuando el programa lo pida.

### Para salir del programa:
Escribí `salir` y presioná Enter.

---

## 📊 ¿Cómo se calcula el puntaje?

| Criterio | Puntaje |
|----------|---------|
| Longitud de 8 a 11 caracteres | +1 |
| Longitud de 12 o más caracteres | +2 |
| Contiene letras mayúsculas | +1 |
| Contiene letras minúsculas | +1 |
| Contiene números | +1 |
| Contiene símbolos especiales | +2 |

**Puntaje máximo: 7 puntos**

> ⚠️ Si la contraseña es muy común (como "123456" o "password"), el puntaje será 0 sin importar su longitud.

---

## ❓ Preguntas frecuentes

**¿El programa guarda mis contraseñas?**
No. El programa no almacena ningún dato. Todo se procesa localmente y se borra al cerrar.

**¿Funciona sin internet?**
Sí, funciona completamente sin conexión a internet.

**¿Puedo analizar varias contraseñas seguidas?**
Sí, el programa te sigue pidiendo contraseñas hasta que escribís `salir`.

---

## 👤 Autor

**Ferreyra Nicolás** – Estudiante de 6° año Técnico en Computación  
GitHub: [@ferreyranicolas125](https://github.com/ferreyranicolas125)
