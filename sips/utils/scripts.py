# -*- coding: utf-8 -*-

a = """Acatic
Acatlán de Juárez
Ahualulco de Mercado
Amacueca
Amatitán
Ameca
Arandas
Atemajac de Brizuela
Atengo
Atenguillo
Atotonilco el Alto
Atoyac
Autlán de Navarro
Ayotlán
Ayutla
Bolaños
Cabo Corrientes
Cañadas de Obregón
Casimiro Castillo
Chapala
Chimaltitán
Chiquilistlán
Cihuatlán
Cocula
Colotlán
Concepción de Buenos Aires
Cuautitlán de García Barragán
Cuautla
Cuquío
Degollado
Ejutla
EL Arenal
El Grullo
El Limón
El Salto
Encarnación de Díaz
Etzatlán
Gómez Farías
Guachinango
Guadalajara
Hostotipaquillo
Huejúcar
Huejuquilla el Alto
Ixtlahuacán de los Membrillos
Ixtlahuacán del Río
Jalostotitlán
Jamay
Jesús María
Jilotlán de los Dolores
Jocotepec
Juanacatlán
Juchitlán
La Barca
La Huerta
La Manzanilla de la Paz
Lagos de Moreno
Magdalena
Mascota
Mazamitla
Mexticacán
Mezquitic
Mixtlán
Ocotlán
Ojuelos de Jalisco
Pihuamo
Poncitlán
Puerto Vallarta
Quitupan
San Cristóbal de la Barranca
San Diego de Alejandría
San Gabriel
San Juan de los Lagos
San Juanito de Escobedo
San Julián
San Marcos
San Martín de Bolaños
San Martín Hidalgo
San Miguel el Alto
San Sebastián del Oeste
Santa María de los ?ngeles
Santa María del Oro
Sayula
Tala
Talpa de Allende
Tamazula de Gordiano
Tapalpa
Tecalitlán
Techaluta de Montenegro
Tecolotlán
Tenamaxtlán
Teocaltiche
Teocuitatlán de Corona
Tepatitlán de Morelos
Tequila
Teuchitlán
Tizapán el Alto
Tlajomulco de Zúñiga
Tlaquepaque
Tolimán
Tomatlán
Tonalá
Tonaya
Tonila
Totatiche
Tototlán
Tuxcacuesco
Tuxcueca
Tuxpan
Unión de San Antonio
Unión de Tula
Valle de Guadalupe
Valle de Juárez
Villa Corona
Villa Guerrero
Villa Hidalgo
Villa Purificación
Yahualica de González Gallo
Zacoalco de Torres
Zapopan
Zapotiltic
Zapotitlán de Vadillo
Zapotlán del Rey
Zapotlán el Grande
Zapotlanejo"""

municipios = a.split('\n')

for m in municipios:
    print ("INSERT INTO asuntos_municipio (name) values('%s');" % m)