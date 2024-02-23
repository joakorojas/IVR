from models.llamada import Llamada
from models.cliente import Cliente
from db_singleton import session

llamada1 = Llamada.getById(session, 1)
print(llamada1)


id = llamada1.getId()
fecha = llamada1.getFecha()
descri = llamada1.getDescripcionOperador()
accion = llamada1.getDetalleAccion()
dura = llamada1.getDuracion()
encu = llamada1.getEncuestaEnviada()
audi = llamada1.getObservacionAuditor()
idC = llamada1.getIdCliente()

print(id)
print(fecha)
print(descri)
print(accion)
print(dura)
print(encu)
print(audi)
print(idC)