//CODIGO REALIZADO POR HECTOR TORIBIO GONZALEZ
public class pruebas {

    /*
     * Programa al que le introduces un array de vectores y te saca el mismo array
     * pero con los angulos respecto de otro vector. Lo he utilizado para comprobar
     * si me ordenaba bien los vectores. Los metodos de imprimir vectores de todos
     * los algoritmos estan hechos de manera que se puedan copiar y pegar dentro del
     * vector de este programa
     */
    public static void main(String[] args) {
        double[][] vector = { {} }; // introducir
        // aqui
        // vector
        double[] prueba = { 1, 1 }; // vector de referencia
        imprimeArray(vector, prueba);
    }

    public static void imprimeArray(double[][] vector, double[] prueba) {

        // Recorremos array
        System.out.print("(");
        for (int j = 0; j < vector.length; j++) {

            // Recorremos cada vector para imprimir cada angulo

            System.out.print(sacaAngulo(prueba, vector[j]));

            // Impresion de la separacion de cada angulo
            System.out.print(" || ");

        }
        System.out.print(")");

    }

    // Metodo para sacar cada angulo
    public static double sacaAngulo(double[] vector, double[] comp) {
        return Math.toDegrees(Math.acos(((vector[0] * comp[0]) + (vector[1] * comp[1]))
                / (Math.sqrt(Math.pow(vector[0], 2) + Math.pow(vector[1], 2))
                        * Math.sqrt(Math.pow(comp[0], 2) + Math.pow(comp[1], 2)))));
    }
}