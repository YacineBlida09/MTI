# File: python/tp/tp6/ex2.py
from abc import ABC, abstractmethod

# product abstract y heritiw menou concret comme interface
class Rapport(ABC):
    @abstractmethod
    def generate(self):
        pass
    
    @abstractmethod
    def save(self, filename):
        pass

#Concrete products
class PDFRapport(Rapport):
    def generate(self):
        return "rani n5dm f pdf"
    
    def save(self, nomfich):
        return f"rani nsauvegardi f pdf asmou {nomfich}"
    
    def __str__(self):
        return "rapport PDF"

class WordRapport(Rapport):
    def generate(self):
        return "rani n5dm f word"
    
    def save(self, nomfich):
        return f"rani nsauvegardi f word asmou {nomfich}"
    
    def __str__(self):
        return "rapport WORD"

class ExcelRapport(Rapport):
    def generate(self):
        return "rani n5dm f Excel"
    
    def save(self, nomfich):
        return f"rani nsauvegardi f excel asmou {nomfich}"
    
    def __str__(self):
        return "rapport Excel"

# Factory
class RapportFactory(ABC):
    @abstractmethod
    def create_rapport(self) -> Rapport:
        pass
    
    def generate_and_save_rapport(self, nomfich):
        rapport = self.create_rapport()
        print(f"Created: {rapport}")
        print(rapport.generate())
        print(rapport.save(nomfich))
        return rapport

# concrete factory
class PDFRapportFactory(RapportFactory):
    def create_rapport(self) -> Rapport:
        return PDFRapport()


class ExcelRapportFactory(RapportFactory):
    def create_rapport(self) -> Rapport:
        return ExcelRapport()


class WordRapportFactory(RapportFactory):
    def create_rapport(self) -> Rapport:
        return WordRapport()


# client
def client_code(factory: RapportFactory, nomfich: str):
    rapport = factory.generate_and_save_rapport(nomfich)
    return rapport


if __name__ == "__main__":
    
    pdf_factory = PDFRapportFactory()
    excel_factory = ExcelRapportFactory()
    word_factory = WordRapportFactory()
    
    print("\n generation pdf")
    pdf_rapport = client_code(pdf_factory, "pdf")
    
