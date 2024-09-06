package com.ebeth.androidmaster

fun main(){
    val altura : Float = 1.70F;
    val peso : Float = 68.8F;

    val imc = peso/(altura*altura);

    println("\nSu IMC es: $imc");
}