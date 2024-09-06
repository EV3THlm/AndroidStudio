package Listas

fun main(){
    inmutableList()
}

fun inmutableList(){

    // Lista inmutable
    val readOnly: List<String> = listOf("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo")

    // Lista mutable
    val weekDaysMutable : MutableList<String> = mutableListOf("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo")
    for (i in weekDaysMutable){
        println("Dia: $i");
    }

    println("\n")
    // agregamos elementos a la lista mutable
    weekDaysMutable.add("Dia Nuevo de la semana")

    // volvemos a imprimir
    for (i in weekDaysMutable){
        println("Dia: $i");
    }
}