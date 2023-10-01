<?php
// Datos del vendedor
$sueldoBasico = 600; // Sueldo básico
$porcentajeComision = 7.5; // Porcentaje de comisión
$bonificacionPorHijo = 50; // Bonificación por hijo en edad escolar
$descuentoPorLey = 11; // Porcentaje de descuento por ley

// Datos del mes recordadno que solo es un ejemplo
$importeTotalVendido = 2000; // Importamos el total vendido del mes
$cantidadHijos = 2; // Cantidad de hijos en edad escolar

// Cálculos que se haran
$comision = ($porcentajeComision / 100) * $importeTotalVendido;
$bonificacion = $bonificacionPorHijo * $cantidadHijos;
$sueldoBruto = $sueldoBasico + $comision + $bonificacion;
$descuento = ($descuentoPorLey / 100) * $sueldoBruto;
$sueldoNeto = $sueldoBruto - $descuento;

echo "Comisión: S/. " . $comision . "<br>";
echo "Bonificación: S/. " . $bonificacion . "<br>";
echo "Sueldo Bruto: S/. " . $sueldoBruto . "<br>";
echo "Descuento: S/. " . $descuento . "<br>";
echo "Sueldo Neto: S/. " . $sueldoNeto;
?>