class Areas:
	
	



	def areacuadrado(lado):
		
		
			""" Description Formula para hallar el area del cuadrado
			:type lado: number
			"""
			return "El area del cuadrado es: " + str(lado*lado)

	def areatriangulo(base, altura):
		
			""" Description: Formula para hallar el area del triangulo
			:type base: number
		
			:type altura: number

			"""
			return "El area del triangulo es: " + str((base*altura/2))	

	def arearectangulo(base,altura):

			""" Description Formula para hallar el area del rectangulo
			:type base: number
		
			:type altura: number
		
		
			"""
			return "El area del rectangulo es: " + str(base*altura)

	def arearombo(diagonalM,diagonalm):
		
			""" Description: Formula para hallar el area del rombo
			:type diagonalM: number
		
			:type diagonalm: number
			"""
			return "El area del rombo es: " + str((diagonalM*diagonalm)/2)

	def areatrapecio(baseM,basem,altura):
		
			""" Description: Formula para hallar el area del trapecio
			:type baseM: number
		
			:type basem: number
		
			:type altura: number
			"""
			return "El area del trapecio es: " + str((baseM*basem)/2*altura)



 



class Volumenes:



	def volumencuadrado(arista):
		
			""" Description : Formula para hallar el volumen del cuadrado
			:type arista: number
			"""
			return "El volumen del cuadrado es: " + str(arista*arista*arista)

	def volumenpiramide(arista,altura):
		
			""" Description: Formula para hallar el volumen de la piramide
			:type arista: number
		
			:type altura: number        
			"""
			return "El volumen de la piramide es: " + str((1/3)*(arista*arista)*altura)


class Perimetros:



	def perimetrocuadrado(arista):
		
			""" Description: Formula para hallar el perimetro del cuadrado

			:type arista: number
				
			"""
			return "El perimetro del cuadrado es: " + str(4*arista)



