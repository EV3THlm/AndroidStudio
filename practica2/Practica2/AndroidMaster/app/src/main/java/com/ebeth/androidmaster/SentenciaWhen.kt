package com.ebeth.androidmaster

fun main(){
    // getMonthConIf(20);
    getMonthConWhen(2);
    getTrimester(2);
}

fun getTrimester(month: Int){
    // en when podemos meter varios valores:
    when(month){
        1, 2, 3 -> println("Primer trimestre");
        4, 5, 6 -> println("Segundo trimestre");
        7, 8, 9 -> println("Tercer trimestre");
        10, 11, 12 -> println("Cuarto trimestre");
        else -> println("¡Trimestre no valido!");
    }
}

fun getMonthConWhen(month: Int){
    // Sentencia when (RECOMENDADA)
    when(month){
        1 -> println("Enero");
        2 -> println("Febrero");
        3 -> println("Marzo");
        4 -> println("Abril");
        5 -> println("Mayo");
        6 -> println("Junio");
        7 -> println("Julio");
        8 -> println("Agosto");
        9 -> println("Septiembre");
        10 -> println("Octubre");
        11 -> println("Noviembre");
        12 -> println("Diciembre");
        else -> println("¡Mes no reconocido!")
    }
}


fun getMonthConIf(month: Int){

    // Condicional comun
    if(month == 1){
        println("\nEnero");
    }
    else if(month == 2){
        println("\nFebrero");
    }
    else if(month == 3){
        println("\nMarzo");
    }
    else if(month == 4){
        println("\nAbril");
    }
    else if(month == 5){
        println("\nMayo");
    }
    else if(month == 6){
        println("\nJunio");
    }
    else if(month == 7){
        println("\nJulio");
    }
    else if(month == 8){
        println("\nAgosto");
    }
    else if(month == 9){
        println("\nSeptiembre");
    }
    else if(month == 10){
        println("\nOctubre");
    }
    else if(month == 11){
        println("\nNoviembre");
    }
    else if(month == 12){
        println("\nDiciembre");
    }
    else{
        println("\n¡El mes no existe!")
    }
}