package com.ebeth.androidmaster

// VARIABLES
fun main(){

    // VAL es para variables mutables (Aquellas que pueden cambiar su valor mas adelante)
    // VAR es para variables INMUTABLES (aquellas que no pueden cambiar su valor)
    print("Ingresa tu nombre: ");
    val nombre: String? = readLine();

    print("Ingresa tu edad: ")
    val edad:Int? = readLine()?.toInt();

    println("\nSu nombre es: $nombre."+
    "\nSu edad es: $edad.")

    println("\nLa suma de 10 y 20 es: ${sumarNumeros(10, 20)}")
}

fun sumarNumeros(numero1: Int, numero2: Int): Int{
    return numero1+numero2
}