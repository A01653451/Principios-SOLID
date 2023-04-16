from MovieInfo import sortMovies, CreateCSV


def main():

    #Obtener la info y organizarla
    sortedMovies = sortMovies()

    #Crear y exportar archivo CSV
    CreateCSV(sortedMovies)


if __name__ == '__main__':
    main()
