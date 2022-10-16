
//CODIGO REALIZADO POR HECTOR TORIBIO GONZALEZ
import java.util.Scanner;

public class QuickShort {

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

        // Algoritmo con un array
        // quickShortUnoAUno(vector, arrayOrd, 0, arrayOrd.length - 1);

        // Algoritmo con dos arrays
        quickShortAngulOrdena(vector, arrayOrd, 0, arrayOrd.length - 1);

        // Finalizamos calculo del tiempo
        double TiempoFin = System.nanoTime();

        // Imprimimos tiempo y array de salida
        System.out.println((TiempoFin - TiempoIn) * Math.pow(10, -9) + " segundos");
        // imprimeArray(arrayOrd);
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

    // Algoritmo quickshort sacando cada ángulo cada vez que se accede al array (1
    // array)
    public static void quickShortUnoAUno(double[] vec, double[][] A, int low, int high) {

        // Si low (que es 0 en un principio) es menor que high (que será el índice al
        // ultimo elemento del array e irá bajando posiciones)
        // Se saca el pivote mediante la función particion
        // y se hacen las dos llamadas recursivas para acotar el vector

        if (low < high) {
            int pivote = particiona(vec, A, low, high);
            quickShortUnoAUno(vec, A, low, pivote - 1);
            quickShortUnoAUno(vec, A, pivote + 1, high);
        }
    }

    // funcion que comprueba los numeros que se tienen que cambiar respecto al
    // pivote y llama a la funcion cambia para cambiarlos
    public static int particiona(double[] vec, double[][] A, int low, int high) {

        // El pivote sera al angulo del ultimo vector del array con el vector de
        // referencia
        double pivote = sacaAngulo(vec, A[high]);
        int i = (low - 1);

        // se recorre el array hasta la ultima posicion
        for (int j = low; j <= high - 1; j++) {

            // si el angulo de la posicion en la que esta j es menos o ygual que el del
            // pivote se cambian la posiciones
            if (sacaAngulo(vec, A[j]) <= pivote) {
                i++;
                cambia(A, i, j);
            }
        }
        cambia(A, i + 1, high);
        return (i + 1);
    }

    // Metodo que cambia dos posiciones del array para la variante de un array
    public static void cambia(double[][] A, int pos1, int pos2) {
        double[] tmp = A[pos1];
        A[pos1] = A[pos2];
        A[pos2] = tmp;
    }

    // Metodo que cambia dos posiciones del array de vectores y dos posiciones del
    // array de angulos para la veriante de dos arrays
    public static void cambia2(double[] aux, double[][] A, int pos1, int pos2) {
        double[] tmp = A[pos1];
        A[pos1] = A[pos2];
        A[pos2] = tmp;

        double tmp2 = aux[pos1];
        aux[pos1] = aux[pos2];
        aux[pos2] = tmp2;
    }

    // Parte del algoritmo que crea el vector de angulos
    public static void quickShortAngulOrdena(double[] vec, double[][] A, int low, int high) {
        // Array que va a almacenar los ángulos de los vectores
        double[] aux = new double[A.length];

        // Inicializamos variable que va a recorrer los arrays
        int i = 0;

        // Sacamos los ángulos de cada vector con el vector de referencia y los metemos
        // todos en el array auxiliar
        while (i < A.length) {
            aux[i] = sacaAngulo(A[i], vec);
            i++;
        }

        quickShort2(aux, A, low, high);
    }

    // El propio algorimo de dos arrays
    public static void quickShort2(double[] aux, double[][] A, int low, int high) {
        // Si low (que es 0 en un principio) es menor que high (que será el índice al
        // ultimo elemento del array e irá bajando posiciones)
        // Se saca el pivote mediante la función particion
        // y se hacen las dos llamadas recursivas para acotar el vector
        if (low < high) {
            int pivote = particiona2(aux, A, low, high);

            quickShort2(aux, A, low, pivote - 1);
            quickShort2(aux, A, pivote + 1, high);
        }
    }

    // Metodo particiona para la variante de dos arrays
    public static int particiona2(double[] aux, double[][] A, int low, int high) {
        int i = (low - 1);
        double pivote = aux[high];

        for (int j = low; j <= high - 1; j++) {
            if (aux[j] <= pivote) {
                i++;

                cambia2(aux, A, i, j);
            }
        }
        cambia2(aux, A, i + 1, high);
        return (i + 1);
    }

    // Funcion que saca el angulo entre dos vectores que le son pasados como
    // parametros
    public static double sacaAngulo(double[] vector, double[] comp) {
        return Math.toDegrees(Math.acos(((vector[0] * comp[0]) + (vector[1] * comp[1]))
                / (Math.sqrt(Math.pow(vector[0], 2) + Math.pow(vector[1], 2))
                        * Math.sqrt(Math.pow(comp[0], 2) + Math.pow(comp[1], 2)))));
    }
}