0x18-webstack_monitoring


# Para validar el funcionamiento del dataDog en el server 

##Modificar el API-Key y el APPLICATION-KEY

Una vez creada sus keys (app y api) y agregadas a la intranet puede hacer la siguiente prueba:

curl -X GET "https://api.datadoghq.com/api/v1/hosts" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: 324a9c938fa96ced070356cb010097fb" \
-H "DD-APPLICATION-KEY: 56289a84146cbea9d287a72bad6a5b3ef4e12c39"



Para validar y ver la kask 2 

curl -X GET "https://api.datadoghq.com/api/v1/dashboard" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: 324a9c938fa96ced070356cb010097fb" \
-H "DD-APPLICATION-KEY: 56289a84146cbea9d287a72bad6a5b3ef4e12c39"
