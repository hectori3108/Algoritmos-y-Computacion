
//CODIGO REALIZADO POR HECTOR TORIBIO GONZALEZ
import java.util.Scanner;

public class QuickShortM1 {

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
        quickShortUnoAUno(vector, arrayOrd, 0, arrayOrd.length - 1, 10);
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

    // Algoritmo quickshort sacando cada ángulo cada vez que se accede al array
    public static void quickShortUnoAUno(double[] vec, double[][] A, int low, int high, int c) {

        // comprobamos si al array en este momento es menor que la constante
        if (high - low + 1 > c) {

            // si low es menor que high, recursividad
            if (low < high) {
                int pivote = particiona(vec, A, low, high);
                quickShortUnoAUno(vec, A, low, pivote - 1, c);
                quickShortUnoAUno(vec, A, pivote + 1, high, c);

            }

            // Si es menor que la constante pasa a inserción directa
        } else {
            A = insercionUnoAUno(A, vec, low, high);
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

    // Funcion que saca el angulo entre dos vectores que le son pasados como
    // parametros
    public static double sacaAngulo(double[] vector, double[] comp) {
        return Math.toDegrees(Math.acos(((vector[0] * comp[0]) + (vector[1] * comp[1]))
                / (Math.sqrt(Math.pow(vector[0], 2) + Math.pow(vector[1], 2))
                        * Math.sqrt(Math.pow(comp[0], 2) + Math.pow(comp[1], 2)))));
    }

    // Insercion modificada que recorre desde low hasta high para la segunda
    // modificacion
    public static double[][] insercionUnoAUno(double[][] desord, double[] vector, int low, int high) {

        // Ponemos la variable i a low para empezar a ordenar el array
        int i = low;

        // Inicializamos j que nos va a servir para comparar la posición en la que
        // estemos del array con la posición anterior
        int j;

        // Inicializamos x e y en las que vamos a almacenar la posición actual en la que
        // estamos por si vamos a necesitar cambiarla con la anterior
        double x;
        double[] y;

        // Comienzo de la ordenación
        // While que recorre el array desde la segunda posición hasta high
        while (i <= high) {

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
                j--;
            }
            desord[j + 1] = y;
            i++;
        }
        return desord;
    }
}