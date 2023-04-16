# Building project locally
Install VirtualEnvironment (one time)

    >python -m pip install virtualenv

Create virtual environment

    >virtualenv virtual_project

1. This will create a virtual environment project folder and install python there.
2. This step can be skipped if you already have the folder locally.

Open virtual environment (Unix type OS)

    >source virtual_project/bin/activate

1. This will activate the virtual environment.  Yous should see `(virtual_project)` to the left of the terminal prompt.
2. This step will be needed each time.

Install requirements
    
    >python -m pip install -r requirements.txt

Install local src/ folder

    >python -m pip install -e src 

# Building Docker image
At the root of the project run

    >docker image build -t YOUR_NAME .

This will create a docker image using the `Dockerfile` with the image name `YOUR_NAME`

Run container

    >docker run YOUR_NAME

#SOLID

Se creo un nuevo archivo .py en donde se extrae la información de las películas y en donde se implementan 2 funciones:
    SortMovies(): En donde se organiza la información de las películas en un array.

    CreateCSV(): La cual recibe un parámetro el cual contenga la información de las películas ordenadas para poder       exportar un archivo CSV donde se encontrará toda la información.

Esto se hizo para simplificar el código principal y poder tener mayor control sobre los componentes en caso de querer modificarlos, además de poder utilizar los métodos en el futuro de manera independiente.
