"""
Desafío 1: Palíndromos

"""
class Validador_Palindromos:
     # Verifica si la cadena es un palíndromo.
     # s: str indica que se espera texto; -> bool indica un resultado True o False.
    def esPalindromo(self,s: str)-> bool:
    # Dos índices: l comienza a la izquierda y r a la derecha.
        l, r= 0,len(s)-1
        # Compara los extremos mientras los índices no se encuentren o crucen.
        while l < r:
            # Avanza por la izquierda, ignorando espacios y signos.
            while l<r and not self.alfanum(s[l]):
                l+=1
            # Retrocede por la derecha, ignorando espacios y signos.
            while r>l and not self.alfanum(s[r]):
                r-=1
            # Convierte ambos caracteres a minúsculas para compararlos.
            # Si son diferentes, la cadena no es un palíndromo.
            if s[l].lower()!=s[r].lower():
                return False
            # Mueve ambos índices hacia el centro.
            l,r=l+1,r-1
        # Si no se encontraron diferencias, es un palíndromo.
        return True        

    def alfanum(self,c):
        return c.isalnum()

# Solicita al usuario la frase que desea evaluar.
frase = input("Escribe una frase: ")
# Crea un objeto de la clase, evalúa la frase y muestra el resultado.
print("Es palíndromo" if Validador_Palindromos().esPalindromo(frase)
      else "No es palíndromo")