from django.db import models

# Create your models here.

class Warehouse (models.Model):
    name = models.CharField (max_length = 200)

    def __str__ (self):
        return self.name

class WarehouseLocation(models.Model):
    name = models.CharField(max_length = 200)

    def __str__ (self):
        return self.name

class AddWare (models.Model):
    name = models.CharField (max_length = 200)

    id = models.AutoField (primary_key= True)

    description = models.CharField (max_length = 700, null = True)

    price = models.DecimalField (max_digits = 10, decimal_places = 2, null = True, blank = True)

    imported_quantity = models.IntegerField (default = 0)

    image = models.ImageField(upload_to = 'images/')

    imported = models.BooleanField(default = False)

    exported = models.BooleanField(default = False)

    warehouse_from = models.ForeignKey(Warehouse, on_delete = models.CASCADE, null = True)

    warehouse_loc = models.ManyToManyField (WarehouseLocation)

    warehouse = models.CharField (max_length = 100)

    order_received = models.DateField (blank = True, null = True)

    

    def __str__ (self):
        return self.name
        

#Funkcja przyjmowania towaru na magazyn. Zawiera: Nazwę, kod, opis, cenę, ilość i docelowy magazyn


    # pamiętaj o zaimportowaniu modeli
    #Stwórz modele odpowiadające elementom modelu AddWare
#Funkcja generowania raportu przyjęcia towaru. Zawiera dane z funkcji przyjęcia towaru na magazyn oraz datę i dodatkowe informacje dotyczące przyjęcia towaru.
#Postępuj wg informacji na stronie https://django-import-export.readthedocs.io/en/latest/getting_started.html
#Stworzono model pod dodawanie towaru z importu, następnie trzeba będzie zrobić formularz w bazie danych i na stronie