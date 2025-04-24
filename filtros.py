from PIL import Image, ImageFilter, ImageOps

def filtro_negativo(img):
    return ImageOps.invert(img.convert("RGB"))

def filtro_mediana(img):
    return img.filter(ImageFilter.MedianFilter(size=3))

def filtro_gaussiano(img):
    return img.filter(ImageFilter.GaussianBlur(radius=2))

def filtro_pb(img):
    """Converte a imagem para preto e branco (binária)"""
    return img.convert('L').point(lambda x: 0 if x < 128 else 255, '1')

def filtro_contorno(img):
    """Detecta contornos simples"""
    return img.filter(ImageFilter.CONTOUR)
