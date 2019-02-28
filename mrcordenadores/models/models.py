# -*- coding: utf-8 -*-

from odoo import models, fields, api
class ordenador(models.Model):
    _name = 'mrcordenadores.ordenador'
    name = fields.Char(string = "Codigo",required = True)
    nombre = fields.Char(String= "Nombre del equipo", required = True)
    estado = fields.Selection( [('0','Disponible'),('1',"Averiado"), ('2','En reparacion')],string = "Estado",default="0", required= True)
    empleado = fields.One2many("mrcordenadores.empleado","ordenador",string = "Empleados que usan el ordenador",required= True)
    caracteristicas = fields.Text(string = "caracteristicas Tecnicas del PC")
    precio = fields.Integer(string = "Precio",stored= True,required= True)

    _sql_constraints = [('modelo_unique', 'unique(name)', 'Este id ya existe')]


class tecnico(models.Model):
    _name = 'mrcordenadores.tecnico'

    name = fields.Char(string = "DNI",required= True)
    nombre = fields.Char(string = "Nombre del Tecnico",required= True)
    apellido = fields.Char(string = "Apellido del Tecnico",required= True)
    titulo = fields.Char(string = "Titulo",required= True)
    _sql_constraints = [('modelo_unique', 'unique(name)', 'Este DNI ya existe')]


class empleado(models.Model):
    _name = 'mrcordenadores.empleado'
    name = fields.Char(string = "DNI",required= True)
    nombre = fields.Char(string = "Nombre del empleado",required= True)
    apellido = fields.Char(string = "Apellido del empleado",required= True)
    puesto = fields.Char(string = "Puesto")
    ordenador = fields.Many2one("mrcordenadores.ordenador",string = "Ordenador")
    perfil = fields.Binary()
    _sql_constraints = [('modelo_unique', 'unique(name)', 'Este DNI ya existe')]

class mantenimiento(models.Model):
    _name = "mrcordenadores.mantenimiento"
    name = fields.Char(string = "Codigo",required= True)
    empleado = fields.Many2one("mrcordenadores.tecnico",string = "Tecnico",required= True)
    ordenador = fields.Many2one("mrcordenadores.ordenador",string = "Ordenador",required= True)
    estado = fields.Selection( [('0','Disponible'),('1',"Averiado"), ('2','En reparacion')],string = "Estado",default="0",related = "ordenador.estado",required= True)
    fecha = fields.Date(string = "Fecha de mantenimiento",required= True)
    datos = fields.Text(string ="Datos de mantenimiento",required= True)
    @api.one
    def mandarAReparar(self):
        self.estado = "2"

class reparacion(models.Model):
    _name = "mrcordenadores.reparacion"
    name = fields.Char(string = "Codigo",required= True)
    empleado = fields.Many2one("mrcordenadores.tecnico",string = "Tecnico",required= True)
    ordenador = fields.Many2one("mrcordenadores.ordenador",string = "Ordenador",required= True)
    estado = fields.Selection( [('0','Disponible'),('1',"Averiado"), ('2','En reparacion')],string = "Estado",default="0",related = "ordenador.estado",required= True)
    datos = fields.Text(string ="Datos de la reparacion")
    fecha = fields.Date(string = "Fecha de reparacion")

    @api.one
    def reparar(self):
        self.estado = "0"
