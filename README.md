# ¿Cómo va mi trámite?

### Instrucciones    
* Clonar el repositorio - ```git clone https://github.com/fcopantoja/sips.git```  
* Instalar python 2 - ```https://www.python.org/downloads/windows/```  
* * Panel de control > Sistema y seguridad > Sistema > Configuración avanzada del sistema > Opciones avanzadas > Variables de entorno > Variables del sistema > Path > Editar; Pegamos (";C:\Python27;C:\Python27\Scripts\") {"C:\Python27" es donde se instalo Python 2} > Aceptar.
* Instalar pip - ```https://pip.pypa.io/en/stable/installing/```  
* * Hacer clic en descargar, nos manda a otra página, clic izquierdo > Guardar como... 
* * En cmd dirigirnos a la carpeta donde se guardó y ejecutar comando
* Instalar virtualenv - ```pip install virtualenv```  
* Crear ambiente virtual - ```virtualenv sips``` (Ejecutar en otro directorio, por ejemplo /home/envs)
* * Cualquier otro directorio que no sea el del GitHub
* Activar ambiente virtual MAC OS- ```source sips/bin/activate```  
* Activar ambiente virtual Windows- ```sips/Scripts/activate``` 
* Instalar paquetes: ```pip install -r /path_del_proyecto/sips/requirements.txt```  
* Arrancar proyecto Django: ```python manage.py runserver```  

URL Amazon: http://52.41.46.30:9000/  
Django Admin URL: http://52.41.46.30:9000/admin  

### Instrucciones  
* Para instalar nuevos paquetes: 
* * Activar ambiente virtual 
* * Entrar al directorio del proyecto y correr ```pip install -r requirements.txt```

