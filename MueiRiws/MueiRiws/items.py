# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AcapellasItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()		# Título
    author = scrapy.Field()		# Autor
    date = scrapy.Field()		# Fecha
    duration = scrapy.Field()		# Duración (s)
    genre = scrapy.Field()		# Género (estilo)
    time_signature = scrapy.Field()	# Compás
    key = scrapy.Field()		# Escala
    bpm = scrapy.Field()        # beat per minute
    gender = scrapy.Field()		# Género (sexo)
    file_size = scrapy.Field()		# Tamaño archivo
    usage = scrapy.Field()		# Licencia
    description = scrapy.Field()	# Descripción
    other_tags = scrapy.Field()		# Otros tags
    pass
