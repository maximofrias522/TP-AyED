import pickle
from datos import *
from common import *

def verLikes():
    tam = os.path.getsize(likesDbFisica)
    likesDbLogica.seek(0)
    while likesDbLogica.tell() < tam:
        like = pickle.load(likesDbLogica)
        print(like.idEmisor, like.idReceptor, like.estado)

def verEstudiantes():
    tam = os.path.getsize(estudiantesDbFisica)
    estudiantesDbLogica.seek(0)
    while estudiantesDbLogica.tell() < tam:
        est : Estudiante = pickle.load(estudiantesDbLogica)
        imprimirDatosDeEstudiante(est)
        print(f'Estado: {est.estado}')
        print(f'Superlike: {est.superlike}')
        print(f'Revelar: {est.revelarCandidatos}')
        print('\n')

def verMods():
    tam = os.path.getsize(moderadoresDbFisica)
    moderadoresDbLogica.seek(0)
    while moderadoresDbLogica.tell() < tam:
        mod : Moderador = pickle.load(moderadoresDbLogica)
        print(mod.id)
        print(mod.email)
        print(mod.nombre)
        print(mod.estado)
        print('\n')

def verAdmins():
    tam = os.path.getsize(administradoresDbFisica)
    administradoresDbLogica.seek(0)
    while administradoresDbLogica.tell() < tam:
        admin : Administrador = pickle.load(administradoresDbLogica)
        print(admin.id)
        print(admin.email)
        print(admin.nombre)
        print(admin.estado)
        print('\n')

def verReportes():
    tam = os.path.getsize(reportesDbFisica)
    reportesDbLogica.seek(0)
    while reportesDbLogica.tell() < tam:
        reporte : Reporte = pickle.load(reportesDbLogica)
        print(reporte.idEmisor)
        print(reporte.idReceptor)
        print(reporte.motivo)
        print(reporte.estado)
        print(reporte.idMod)
        print('\n')

def menu():
    print('1. Ver likes')
    print('2. Ver estudiantes')
    print('3. Ver moderadores')
    print('4. Ver administradores')
    print('5. Ver reportes')
    op = input('Seleccionar opción: ')
    if op == '1':
        verLikes()
    elif op == '2':
        verEstudiantes()
    elif op == '3':
        verMods()
    elif op == '4':
        verAdmins()
    elif op == '5':
        verReportes()

menu()