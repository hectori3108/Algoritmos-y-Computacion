
//CODIGO REALIZADO POR HECTOR TORIBIO GONZALEZ
import java.util.Scanner;

public class Insertion {

    public static void main(String[] args) {
        // Inicializamos scanner
        Scanner in = new Scanner(System.in);

        // array de prueba para comprobar si funciona
        // double[][] arrayOrd = { { 4, 6 }, { 3, 4 }, { 8, 9 }, { 5, 6 }, { 4.5, 0.3 },
        // { 9.8, 7.2 }, { 4.1, 8.5 },
        // { 1.1, 6.8 }, { 4.4, 5.8 }, { 4, 7.7 } };

        // Bucle para que el usuario intruduzca el número de vectores random que quiere
        // en el array

        System.out.print("Introduzca el tamaño del vector: ");
        int tamano = in.nextInt();
        double[][] arrayOrd = new double[tamano][2];
        for (int i = 0; i < tamano; i++) {
            arrayOrd[i][0] = Math.random() * 10;
            arrayOrd[i][1] = Math.random() * 10;
        }

        // Inicializamos el vector de referencia y el usuario introduce las componentes
        // de éste
        double[] vector = { 0, 0 };
        System.out.println(
                "A continuación vamos a implementar un algoritmo para odenar un array de vectores de menor a mayor ángulo repecto otro ángulo seleccionado por el usuario");
        System.out.println("Introduzca la primera coordenada del ángulo: ");
        vector[0] = in.nextDouble();
        System.out.println("Introduzca la segunda coordenada del ángulo: ");
        vector[1] = in.nextDouble();

        // Impresión de array sin ordenar
        System.out.print("El array sin ordenar es el siguiente  ");
        // imprimeArray(arrayOrd);
        System.out.println("\nOrdenando...");
        System.out.println("\nVector ordenado: ");

        // comenzamos a calcular el tiempo
        double TiempoIn = System.nanoTime();

        /* ALGORITMOS */
        arrayOrd = insercionUnoAUno(arrayOrd, vector);
        // arrayOrd = insercionAngulOrdena(arrayOrd, vector);

        // Finalizamos calculo del tiempo
        double TiempoFin = System.nanoTime();

        // Imprimimos tiempo y array de salida
        System.out.println((TiempoFin - TiempoIn) * Math.pow(10, -9) + " segundos");
        imprimeArray(arrayOrd);
    }

    /*********************************************
     * ALGORITMOS
     *********************************************/

    // Algoritmo para imprimir array
    public static void imprimeArray(double[][] vector) {

        // Recorremos array
        for (int j = 0; j < vector.length; j++) {
            System.out.print("{");

            // Recorremos cada vector para imprimir cada componente
            for (int i = 0; i < 2; i++) {
                System.out.print(vector[j][i]);

                // Impresion de las comas de dentro de cada vector
                if (i != 1) {
                    System.out.print(",");
                }
            }
            System.out.print("}");

            // Impresion de las comas que separan cada vector
            if (j != vector.length - 1) {
                System.out.print(",");
            }

        }
    }

    // Algoritmo que calcula primero todos los ángulos y ordena seguidamente el
    // array de ángulos a la vez que el array de vectores
    public static double[][] insercionAngulOrdena(double[][] desord, double[] vector) {

        // Array que va a almacenar los ángulos de los vectores
        double[] aux = new double[desord.length];

        // Inicializamos variable que va a recorrer los arrays
        int i = 0;

        // Sacamos los ángulos de cada vector con el vector de referencia y los metemos
        // todos en el array auxiliar
        while (i < desord.length) {
            aux[i] = sacaAngulo(desord[i], vector);
            i++;
        }

        // Ponemos la variable i a 1 para empezar a ordenar los arrays
        i = 1;

        // Inicializamos j que nos va a servir para comparar la posición en la que
        // estemos del array con la posición anterior
        int j;

        // Inicializamos x e y en las que vamos a almacenar la posición actual en la que
        // estamos por si vamos a necesitar cambiarla con la anterior
        double x;
        double[] y;

        // Comienzo de la ordenación
        // While que recorre los array desde la segunda posición hasta el final
        while (i < aux.length) {

            // Guardamos el angulo en el que estamos y el vector del array
            x = aux[i];
            y = desord[i];

            // j va a referirse a la posicion anterior a la que estamos
            j = i - 1;

            // Mientras j no esté fuera del array y los vectores/angulos deban cambiarse...
            while (j >= 0 && aux[j] > x) {

                // la posicion actual pasa a ser la anterior
                aux[j + 1] = aux[j];
                desord[j + 1] = desord[j];

                // miramos todas las posiciones por detras de i para comprobar que no haya
                // ninguno mayor que él
                j--;
            }

            aux[j + 1] = x;
            desord[j + 1] = y;
            i++;
        }
        return desord;

    }

    // Algoritmo que calcula loa ángulos a la vez que va ordenando el array
    public static double[][] insercionUnoAUno(double[][] desord, double[] vector) {

        // Ponemos la variable i a 1 para empezar a ordenar el array
        int i = 1;

        // Inicializamos j que nos va a servir para comparar la posición en la que
        // estemos del array con la posición anterior
        int j;

        // Inicializamos x e y en las que vamos a almacenar la posición actual en la que
        // estamos por si vamos a necesitar cambiarla con la anterior
        double x;
        double[] y;

        // Comienzo de la ordenación
        // While que recorre el array desde la segunda posición hasta el final
        while (i < desord.length) {

            // Sacamos el ángulo de esa posicion
            x = sacaAngulo(desord[i], vector);

            // Guardamos en y el vector de esa posicion por si lo necesitamos para cambiarlo
            y = desord[i];

            // j va a referirse a la posicion anterior a la que estamos
            j = i - 1;

            // Mientras j no se salga del array y el angulo sacado de la posicion i sea
            // menos que el sacado en la posicion j(lo sacamos en el propio while)
            while (j >= 0 && (sacaAngulo(desord[j], vector) > x)) {

                // la posicion actual pasa a ser la anterior
                desord[j + 1] = desord[j];

                // miramos todas las posiciones por detras de i para comprobar que no haya
                // ninguno mayor que él
                j -= 1;
            }
            desord[j + 1] = y;
            i += 1;
        }
        return desord;
    }

    // Funcion que saca el angulo entre dos vectores que le son pasados como
    // parametros
    public static double sacaAngulo(double[] vector, double[] comp) {
        return Math.toDegrees(Math.acos(((vector[0] * comp[0]) + (vector[1] * comp[1]))
                / (Math.sqrt(Math.pow(vector[0], 2) + Math.pow(vector[1], 2))
                        * Math.sqrt(Math.pow(comp[0], 2) + Math.pow(comp[1], 2)))));
    }
}
