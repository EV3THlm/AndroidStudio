package com.ebeth.androidmaster

fun main(){
    // Ejemplos de funciones
    showMyName("Estefany")
    showMyAge(19)
    add(25, 25)
    println(resta(100, 10))
}

// Funcion basica
fun showMyName(name: String){
    println("¡Hola!, me llamo $name")
}

// Funcion con parametros de entrada
fun showMyAge(currentAge: Int){
    println("Tengo $currentAge")
}

fun add(firstNumber: Int, secondNumber: Int){
    println(firstNumber + secondNumber)
}

// Funciones con parametros de salida
fun resta(numero1:Int, numero2:Int): Int{
    return numero1-numero2
}