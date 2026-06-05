#!/bin/bash
echo "Generando tráfico de prueba..."
for i in {1..50}
do
  curl -s http://localhost:8080/ > /dev/null
  curl -s http://localhost:8080/recetas > /dev/null
  curl -s http://localhost:8080/health > /dev/null
  echo "Request $i enviado"
  sleep 0.5
done
echo "Tráfico generado exitosamente"