package Arrays

fun main(){
    val weekDays= arrayOf("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo")
    println(weekDays.size)

    for(i in weekDays){
        if(i=="Lunes"){
            println("El dia es: $i")
        }
        break
    }
}