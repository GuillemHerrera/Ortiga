.. _SistemesCoordenades:

***********************************
Gestió dels Sistemes de Coordenades
***********************************

QGis per defecte assigna el CRS EPSG:4326 als nous projectes que s'inicien.

Així doncs hem assignar-li el nostre amic 25831 al nou projecte per poder fer els caculs correctes en les geometries que afegirem més endavant.

Tenim tres maneres de fer-ho:

1. Pestanya "Projecte" -> "Propietats" -> "CRS"
	Obrim les preferencies generals del projecte

.. image:: _static/qgis-img/Project_Properties_CRS.png
	:align: center

1. El botó de Sistemes de Coordenades de la Barra inferior
	Ens obre el mateix menu de gestio del CRS del Projecte que la opció anterior
	
.. image:: _static/qgis-img/SetProjectCRS_bb.png
	:align: center


2. Menú contextual de la capa (Botó dret) -> Set CRS -> Set Project CRS from Layer
	Aquest opció assigna el CRS de la capa al projecte 

.. image:: _static/qgis-img/SetProjectCRS.png
	:align: center


.. note:: Podem barrejar CRS en un mateix projecte, tot i que hem de anar en compte si fèssim anàlisis
 espaials. Per al que ens toca ara, només saber que els mapes base poden estar sense problemes amb EPSG:4326