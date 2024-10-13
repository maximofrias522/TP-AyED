import sys
from datos import *
from interfaz import *
from common import *
from rich.table import Table

modderActual = Moderador()

def menuModerador(usuario): # menu principal
    global modderActual
    modderActual = usuario
    mostrarMenuMod()
    opcion = input('Seleccione una opción: ')
    
    while opcion != '0':
        if opcion == '1':
            gestionarUsuarios()
        elif opcion == '2':
            gestionarReportes()
        elif opcion == '3':
            reportesEstadisticos()
        else:
            opcionInvalida()

        mostrarMenuMod()
        opcion = input('Seleccione una opción: ')


def gestionarUsuarios():
    mostrarGestionarUsuariosMod()
    opcion = input('Seleccione una opción: ')
    
    while opcion != '0':
        if opcion == '1':
            eliminarUsuario()
        else:
            opcionInvalida()
        mostrarGestionarUsuariosMod()
        opcion = input('Seleccione una opción: ')


def gestionarReportes():
    mostrarGestionarReportes()
    opcion = input('Seleccione una opción: ')

    while opcion != '0':
        if opcion == '1':
            verReportes()
        else:
            opcionInvalida()
        mostrarGestionarReportes()
        opcion = input('Seleccione una opción: ')

def verReportes():
    console = Console()

    print("Reportes de prueba agregados al archivo.")

    table = Table(title="Tabla de Reportes")

    table.add_column("ID Emisor", style="bold blue")
    table.add_column("ID Receptor", style="bold red", justify="right")
    table.add_column("Motivo", style="bold red", justify="right")
    table.add_column("Estado", style="bold yellow", justify='right')

    with open("estudiantesDbFisica", "rb") as estudiantesDbLogica:
        tames = os.path.getsize("estudiantesDbFisica")
        estudiantesDbLogica.seek(0)  

        with open("reportesDbFisica", "rb") as reportesDbLogica:
        
            tam = os.path.getsize("reportesDbFisica")
            reportesDbLogica.seek(0)  

            while reportesDbLogica.tell() < tam:
                try:
                
                    reporte = pickle.load(reportesDbLogica)
                    
    
                    estado_emisor = False
                    estado_receptor = False

                    estudiantesDbLogica.seek(0)

                    while estudiantesDbLogica.tell() < tames:
                        estudiante = pickle.load(estudiantesDbLogica)

                        if estudiante.id == reporte.idEmisor:
                            estado_emisor = estudiante.estado

                    
                        if estudiante.id == reporte.idReceptor:
                            estado_receptor = estudiante.estado

                        if estado_emisor and estado_receptor:
                            break

                    if estado_emisor and estado_receptor:
                        table.add_row(str(reporte.idEmisor), str(reporte.idReceptor), reporte.motivo, str(reporte.estado))

                except EOFError:
                    break

    console.print(table)
    continuar()
    gestionarReportes()

def reportesEstadisticos():
    enConstruccion()

def eliminarUsuario():
    opcion = input('Introduza el ID del usuario a eliminar o -1 para volver: ')
    while opcion != '-1':
        try:
            if esIdValida(opcion):
                estudiante = obtenerUsuario(opcion)
                estudiante.estado = False  

                sobrescribirUsuario(estudiantesDbFisica, estudiantesDbLogica, estudiante)
                console.print('El usuario se eliminó correctamente.', style='green')

                actualizarReportesPorUsuario(opcion, modderActual.id)

                continuar()
            else:
                opcionInvalida()
        except Exception as e:
            console.print(f'Error: {e}', style='red')
            opcionInvalida()
        opcion = input('Introduza el ID del usuario a eliminar o -1 para volver: ')

def actualizarReportesPorUsuario(userId, modderId): 
    with open(reportesDbFisica, "r+b") as archivo_reportes:
        tam = os.path.getsize(reportesDbFisica)
        archivo_reportes.seek(0)  

        while archivo_reportes.tell() < tam:
            try:
                reporte = pickle.load(archivo_reportes)

                if reporte.idReceptor == userId:
                    reporte.estado = 1  
                    reporte.idMod = modderId  

                    archivo_reportes.seek(archivo_reportes.tell() - pickle.dumps(reporte).size) 
                    pickle.dump(reporte, archivo_reportes)  
                    console.print(f'Reporte de ID {reporte.idEmisor} o {reporte.idReceptor} actualizado con ID del moderador: {modderId}.', style='yellow')

            except EOFError:
                break
            except Exception as e:
                console.print(f'Error al actualizar el reporte: {e}', style='red')

