# TAREA 15 SXE 🦟

> [!NOTE]
> **Módulo en Odoo que determina la bebida recomendada basada en el nivel de sueño del alumno. 💤💤💤💤**

### PRIMER PASO (CONFIGURACIÓN) 🥷

> **Creamos la carpeta para el módulo en addons haciendo uso de Scaffold, una vez creada, otorgamos permisos**

```bash
docker exec -it odoo18_app odoo scaffold bebida_zzz /mnt/extra-addons
docker exec -it odoo18_app chmod -R 777 /mnt/extra-addons/bebida_zzz                
```

---

### SEGUNDO PASO (CONFIGURACIÓN) 🤹

> **Modificamos el contenido de ./addons/bebida_zzz/__manifest__.py**

```py
# -*- coding: utf-8 -*-
{
    'name': "Bebida ZZZ",

    'summary': "Módulo que recomienda bebida según nivel de sueño",
    
    'description': """
Módulo que se encarga de recomendarle una bebida específica al alumnado según las horas de sueño
        1-3: Café con leche
        4-6: Café solo largo
        7-9: Café solo larguísimo
        10: Inyección de adrenalina
    """,

    'author': "SAUL",
    'website': "https://github.com/saulmnz",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #],
    'installable': True,
    'application': True,
}
```

---

### TERCER PASO (CONFIGURACIÓN) 🧙‍♂️

> **Modificamos el archivo models.py ( precisamos cambiar todo el contenido, aquí eliminaremos todo el código por defecto, añadiremos un nuevo código que contiene los campos del módulo )**

```py
# -*- coding: utf-8 -*-

from odoo import models, fields, api

class BebidaZzz(models.Model):
    _name = 'bebida.zzz'
    _description = 'REGISTRAMOS TU SUEÑO Y TE RECOMENDAMOS UNA BEBIDA'

    # CAMPO 1: EL NOMBRE DEL ALUMNO
    alumno = fields.Char(
        string='Alumno',
        required=True
    )

    # CAMPO 2: EL NIVEL DE SUEÑO DEL ALUMNO
    nivel_sueno = fields.Integer(
        string='Nivel de sueño',
        required=True,
        help="Valor entre 1 y 10"
    )

    # CAMPO 3: LA BEBIDA RECOMENDADA 
    bebida_recomendada = fields.Char(
        string='BEBIDA RECOMENDADA',
        compute='_compute_bebida',
        store=True,
        readonly=True
    )

    # MÉTODO PARA CALCULAR LA BEBIDA EN FUNCIÓN DEL NIVEL DE SUEÑO DEL PANOLI
    @api.depends('nivel_sueno')
    def _compute_bebida(self):
        for record in self:
            nivel = record.nivel_sueno
            if 1 <= nivel <= 3:
                record.bebida_recomendada = 'Café con leche'
            elif 4 <= nivel <= 6:
                record.bebida_recomendada = 'Café solo largo'
            elif 7 <= nivel <= 9:
                record.bebida_recomendada = 'Café solo larguísimo'
            elif nivel == 10:
                record.bebida_recomendada = 'Inyección de adrenalina'
            else:
                record.bebida_recomendada = 'ERROR: nivel debe ser 1-10'
```

---


### CUARTO PASO (CONFIGURACIÓN)🤺

> **Configuramos el archivo views.xml, define las vistas de formulario y lista, la acción para abrirlas y el menú en la interfaz de Odoo.**

```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
  <data>

    <!-- VISTA DE LISTA -->
    <record id="view_bebida_zzz_list" model="ir.ui.view">
        <field name="name">bebida.zzz.list</field>
        <field name="model">bebida.zzz</field>
        <field name="arch" type="xml">
            <list>
                <field name="alumno"/>
                <field name="nivel_sueno"/>
                <field name="bebida_recomendada"/>
            </list>
        </field>
    </record>

    <!-- VISTA DE FORMULARIO -->
    <record id="view_bebida_zzz_form" model="ir.ui.view">
        <field name="name">bebida.zzz.form</field>
        <field name="model">bebida.zzz</field>
        <field name="arch" type="xml">
            <form>
                <sheet>
                    <group>
                        <field name="alumno" placeholder="Dieguito Clavito"/>
                        <field name="nivel_sueno" placeholder="1 a 10"/>
                        <field name="bebida_recomendada" readonly="1"/>
                    </group>
                </sheet>
            </form>
        </field>
    </record>

    <!-- ABRE LA VISTA LISTA -->
    <record id="action_bebida_zzz" model="ir.actions.act_window">
        <field name="name">Bebidas por Sueñito</field>
        <field name="res_model">bebida.zzz</field>
        <field name="view_mode">list,form</field>
        <field name="view_id" ref="view_bebida_zzz_list"/>
    </record>

    <!-- MENÚ PRINCIPAL -->
    <menuitem id="menu_bebida_zzz_root"
              name="Bebida Sueño"
              sequence="10"/>

    <!-- SUBMENÚ -->
    <menuitem id="menu_bebida_zzz_action"
              name="Registrar Sueño"
              parent="menu_bebida_zzz_root"
              action="action_bebida_zzz"
              sequence="10"/>

  </data>
</odoo>
```
---

### QUINTO PASO (COMPROBACIÓN) 👨‍🍳

> **Para ello debemos entrar en el modo desarrollador de odoo, actualizar la lista de aplicaciones, buscar por el nombre el módulo creado y activarlo**

<img width="500" height="400" alt="image" src="https://github.com/user-attachments/assets/2df9c052-8076-453a-8888-39c2a3c529c7" />

> **Una vez activado el módulo, entramos a él y creamos una demostración de ALUMNO CON SUEÑO 🧟**

<img width="500" height="400" alt="image" src="https://github.com/user-attachments/assets/a3a505ce-d6e7-4f6f-ba70-660ff33c8ab7" />

<img width="500" height="400" alt="image" src="https://github.com/user-attachments/assets/1072a8fb-a382-4f7c-9bf5-2011811ce5cb" />


